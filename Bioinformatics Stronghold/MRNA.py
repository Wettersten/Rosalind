cA = 4
cC = 2
cD = 2
cE = 2
cF = 2
cG = 4
cH = 2
cI = 3
cK = 2
cL = 6
cM = 1
cN = 2
cP = 4
cQ = 2
cR = 6
cS = 6
cT = 4
cV = 4
cW = 1
cY = 2
cStop = 3

protein = "MNLGWSVMWEWPGIKDWVYHHKNECDDVSHHKNLAEPIVYWDMQHKCFICHPKWLKVQFHGRFRPNSKYMYGRRNPGSRERYYFKMHSTEAGGWANKTANWTCQYKGQCLMANVWKFMYAATHEEADHMPPDQPIHAAAPTDTMASCKKHWDLYLPCFQMMIGVLPGLTYQLNIEVDLSLGNPRAYKHMQKQCGHTAPYMCVADASIYNYMWRNCLSCSLTDADADATCDNAFYKKPEYLRVARQNPPSTLWQRTTALEYSENQQKSVNYDDYENFKEEAILRRVHNLFMFFFDLHRISHWHAILWESYWMIYHCYPSEALQENSKMNHCNFMKPHGRLWFILVFCKDYANKHGYHKMPQRKEQGEWDLYQYWFFHDVTYVRSFATDRWKILGKGVWDREDHIYSGRRFATMGFAETIYCPFVRHSSHEGRCDYMPEMNRQYCKSMRMSDFFVGQVDFIIYARNMPFWPEVRYTAREFSSIPQYFQPPNVFWIEHGCFMHIDSHGLTHYNTKLNHHAYLHLFLWTEDDWYMKFNIGKQLSHVITSLNPPSDSNCHEYCWHALHHAWYRGTKLAGWLDNSHAVQPYEQMDGHVGRTGPRRGKSPPFTFFIFRTTAPPYINFYEWDDQEPTPLDNWFVGSSKWSVNMCDNELNHCCTKDYDRPLCYVYSRCAHDWYSIGITPLPCSWCQFIGQPLQTEVECPICEKDQKIHSFDEQTCVNMCETGINVEQMSMTPAHNERNRFLYWCYINTVRFHGYQKKSPDSYFFLDVRGIMMWYASSSEWIQVQDMVRVINNWLLNEMPIGDHNIPPENTMQGNNPSCFTGHHTGDASGEKQIMEPRDCKIVGTCKDQDFCMCHNPVLKEALMIKYQNNKQLNWDYFPDVITTAYVMITCESTLMCTDCIDLLWWTMIPCHQHAFFQIVPISWPHFRSQYAIAAADVHDEENNNMDTESSFKKDIQNRVGLFGTMWMWAIPYVVVRMACYLWTINNQSQQKHNTQMHI"
sumRNA = 1
for i in range(len(protein)):
	if protein[i] == 'A':
		sumRNA = sumRNA * cA
	elif protein[i] == 'C':
		sumRNA = sumRNA * cC
	elif protein[i] == 'D':
		sumRNA = sumRNA * cD	
	elif protein[i] == 'E':
		sumRNA = sumRNA * cE
	elif protein[i] == 'F':
		sumRNA = sumRNA * cF	
	elif protein[i] == 'G':
		sumRNA = sumRNA * cG
	elif protein[i] == 'H':
		sumRNA = sumRNA * cH	
	elif protein[i] == 'I':
		sumRNA = sumRNA * cI
	elif protein[i] == 'K':
		sumRNA = sumRNA * cK	
	elif protein[i] == 'L':
		sumRNA = sumRNA * cL
	elif protein[i] == 'M':
		sumRNA = sumRNA * cM	
	elif protein[i] == 'N':
		sumRNA = sumRNA * cN
	elif protein[i] == 'P':
		sumRNA = sumRNA * cP	
	elif protein[i] == 'Q':
		sumRNA = sumRNA * cQ
	elif protein[i] == 'R':
		sumRNA = sumRNA * cR	
	elif protein[i] == 'S':
		sumRNA = sumRNA * cS
	elif protein[i] == 'T':
		sumRNA = sumRNA * cT		
	elif protein[i] == 'V':
		sumRNA = sumRNA * cV
	elif protein[i] == 'W':
		sumRNA = sumRNA * cW		
	elif protein[i] == 'Y':
		sumRNA = sumRNA * cY	
sumRNA = sumRNA * cStop
sumRNA = sumRNA % 1000000
print sumRNA
#709376