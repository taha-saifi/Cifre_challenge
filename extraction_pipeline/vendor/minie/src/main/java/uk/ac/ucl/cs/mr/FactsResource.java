package uk.ac.ucl.cs.mr;

import java.util.List;
import java.util.ArrayList;

import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import de.uni_mannheim.minie.MinIE;
import de.uni_mannheim.minie.annotation.AnnotatedPhrase;
import de.uni_mannheim.minie.annotation.AnnotatedProposition;
import de.uni_mannheim.utils.coreNLP.CoreNLPUtils;

import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.semgraph.SemanticGraph;
import edu.stanford.nlp.semgraph.SemanticGraphCoreAnnotations.BasicDependenciesAnnotation;
import edu.stanford.nlp.util.CoreMap;

/**
 * @author Pasquale Minervini
 */

@Path("/query")
public class FactsResource {

    private static final StanfordCoreNLP parser = CoreNLPUtils.StanfordDepNNParser();

    @POST
    @Produces({MediaType.APPLICATION_JSON})
    public FactsBean query(String input) {
        List<Fact> facts = new ArrayList<>();
        List<String> failedSentences = new ArrayList<>();
        Annotation document = new Annotation(input);
        FactsResource.parser.annotate(document);
        for (CoreMap annotatedSentence : document.get(SentencesAnnotation.class)) {
            String sentence = annotatedSentence.toString();
            SemanticGraph graph = annotatedSentence.get(BasicDependenciesAnnotation.class);
            if (graph == null) continue;
            try {
                MinIE minie = new MinIE(sentence,
                        CoreNLPUtils.semanticGraphUniversalEnglishToEnglish(graph), MinIE.Mode.SAFE);
                for (AnnotatedProposition ap: minie.getPropositions()) {
                    List<AnnotatedPhrase> triple = ap.getTriple();
                    String s = triple.get(0).toString();
                    String p = triple.get(1).toString();
                    String o = triple.get(2).toString();
                    facts.add(new Fact(s, p, o, sentence));
                }
            } catch (RuntimeException ex) {
                // One malformed sentence must not make the whole batch fail.
                failedSentences.add(sentence);
            }
        }

        return new FactsBean(facts, failedSentences);
    }
}
