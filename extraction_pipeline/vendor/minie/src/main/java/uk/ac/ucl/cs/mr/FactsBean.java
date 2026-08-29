package uk.ac.ucl.cs.mr;

import java.util.List;

import javax.xml.bind.annotation.XmlRootElement;

/**
 * @author Pasquale Minervini
 */

@XmlRootElement
public class FactsBean {

    public List<Fact> facts;
    public List<String> failedSentences;

    public FactsBean(List<Fact> facts, List<String> failedSentences) {
        this.facts = facts;
        this.failedSentences = failedSentences;
    }

}
