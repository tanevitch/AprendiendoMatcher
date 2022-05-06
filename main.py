from ontologywrapper import OntologyWrapper
from matcher import SimpleMatcher

ontologia = OntologyWrapper()

# ----------------------------------------------------------------------------------------
# INDIVIDUALS CARGADOS A MANOPLA
# ----------------------------------------------------------------------------------------

ontologia.add_individual("luciana", "Person")
ontologia.add_individual("luciana", "Person")
ontologia.add_individual("juan", "Person")
ontologia.add_individual("install git", "Requirement")
ontologia.add_individual("install virtualenv", "Requirement")
ontologia.add_individual("clone project", "Requirement")


ontologia.add_object_property("install git", "hasAssigned", "juan")
ontologia.add_object_property("install virtualenv", "hasAssigned", "luciana")
ontologia.add_object_property("clone project", "hasAssigned", "luciana")

ontologia.add_object_property("clone project", "dependsOn", "install virtualenv")
ontologia.add_object_property("install virtualenv", "dependsOn", "install git")

# ----------------------------------------------------------------------------------------
# INDIVIDUALS CARGADOS CON SPACY 
# ----------------------------------------------------------------------------------------

matcher = SimpleMatcher()
matcher.add_pattern("nsubj", [[
    {
        "DEP": "nsubj"
    }
]])
matcher.add_pattern("verb", [[
    {
        "POS": "VERB"
    }
]])
matcher.add_pattern("dobj_and_mod", [[
    {
        "POS": "ADJ"
    },
    {
        "DEP": "dobj"
    }
]])

sentence= "Maria executes the main file."
matches= matcher.get_matches(sentence)

maria= "".join(matches["nsubj"])
executes_the_main_file= "".join(matches["verb"]) + " "+ "".join(matches["dobj_and_mod"])
ontologia.add_individual(maria, "Person")
ontologia.add_individual(executes_the_main_file, "Requirement")
ontologia.add_object_property(executes_the_main_file, "dependsOn", "install virtualenv")
ontologia.add_object_property(executes_the_main_file, "hasAssigned", maria)

# ----------------------------------------------------------------------------------------
ontologia.persist()

