class diagnosis:
  def __innit__(self, name, tests, differentialDiagnoses, treatment, prognosis):
    self.name = name
    self.tests = tests
    self.differentialDiagnoses = differentialDiagnoses
    self.treatment = treatment
    self.prognosis = prognosis

diabetes = diagnosis("diabetes","A1C test, blood sugar tests, oral glucose tolerance test.","hyperglycemia, endocrine disorders, pancreatic diseases.","insulin, diet alterations.","potential for strokes, nerve & kidney damage, vision loss, and a requirment to track insulin.")
