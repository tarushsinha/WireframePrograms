myName = "Tarush"
sampleEmail = """To Whom This May Concern:
z
This is where I would show you I have a lot of important stuff to say. But in the place of that, you're going to get
some good old Lore Ipsum stuff!

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sagittis maximus elit. In sit amet tincidunt nisl. Nunc 
nisl tellus, dignissim congue tempus eu, sollicitudin non magna. Duis pretium sed velit eu condimentum. Nullam malesuada
iaculis mollis. Nam sed iaculis erat. Quisque feugiat ut libero id aliquam. Integer consequat libero sed turpis 
ullamcorper dapibus. Integer eget tortor ac erat interdum egestas ultricies in sapien. Nullam tristique et nunc sed 
bibendum. 

Best Regards,
{myName}""".format(myName=myName)


def validEmail(msg, name):
    ret = "Valid"
    if not (msg.startswith("Dear")):
        ret = "Fail - bad start"
    if not (msg.endswith(name)):
        if ret != "Valid":
            ret = ret + " and bad end"
        else:
            ret = "Fail - bad end"
    print(ret)


validEmail(sampleEmail, myName)