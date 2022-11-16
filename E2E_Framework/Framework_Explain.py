"""
FRAMEWORK
--> Is a guideline to be followed while creating test script
-->BDD,DD,Hybrid,KD,POM
-->Base:Basic or the crux of the code is available (Browser)
-->Common Files:
-->Util Files (Any miscellenous activity)
-->Configuration data:Locators(Identifying individual web elements uniquely)
        :ID,NAME,CLASS,CSS,XPATH,LINKTEXT,PARTIAL LINK TEXT,TAGNAME
        :Property files,Test Images,Excel file,Csv files
-->Pages :Each and every pages
-->Whatever actions we need to perform on the respective pages, we add a function in that page file
-->A -- 10 actions , B-->5 actions


"""
"""
PYTEST RULES:
1.The files starting from test_* | *_test will be only considered for test cases
2.The function or test cases starting from test_* | *_test will be considered for test case
3.The classes starting from test_* | *_test will be only considered for test cases

"""

