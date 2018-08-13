while True:
	input_st=input("Input s and t (separated by a whitespace):")
#-------------------------------
	if input_st=="bye":#to detect whether user enter "bye"
		break
#-------------------------------
#to separate the string into two
	i=0
	while input_st[i:i+1]!=" ":
		i=i+1
	s,t=input_st[:i],input_st[i+1:]
#-------------------------------
	length_s,length_t,js,kt,true_false=len(s),len(t),0,0,0
	while js<length_s :
		s1=s[js:js+1]#collect the letter in sequence
		while kt<length_t:
			t1=t[kt:kt+1]
			if s1==t1:
				true_false=true_false+1
				kt=kt+1
				break
			else:
				kt=kt+1
		js+=1
	if true_false==length_s :
		print("Yes")
		print("============================================================")
	else:
		print("No")
		print("============================================================")
	









