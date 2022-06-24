import summary

import runexp

memo = "multi_phase/sumo/pipeline"
runexp.main(memo)
print("****************************** runexp ends (generate, train, test)!! ******************************")
summary.main(memo)
print("****************************** summary_detail ends ******************************")
