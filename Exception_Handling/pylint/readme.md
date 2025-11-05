### Unlike unittest package in pylint we don't design tests or do anything much complex it simply checks your file on which you are running pylint and returns relevan info about your bugs which helps you to resolve those bugs

# And always remember if you won't add -r y at last then pylint won't display the full report for the test if you want complete details of the test add -r y at last -r(indicates report) and then y(indicates yes I want report). If you don't want report and -r n or just write pylint <file_name>
<!-- Cmd command to use pylint -->
pylint <file_name> -r y 
<!-- for example -->
pylint calculator.py -r y

