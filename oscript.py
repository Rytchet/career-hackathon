from panel.models import Event
import datetime

output = [['Pop-Up Career Studio', 'Come and find out more about our 2019 opportunities from the PwC recruitment team and our recent joiners, as well as grabbing a free hot drink!', 'Mon, 11 Feb 2019 10:00:00 ', 'Mon, 11 Feb 2019 14:00:00', 'Liverpool Campus, University Square, Outside the Career Studio'], ['KnowHow - Getting Started with Statistics', "We're taking the Career Studio out onto campus! Look out for the team at our pop-up studio and enter our #Classof2019 competition to win an iPad.", 'Mon, 11 Feb 2019 10:00:00 ', 'Mon, 11 Feb 2019 13:30:00', 'Liverpool Campus, Electrical Engineering &amp; Electronics, Entrance Foyer'], ['KnowHow - Critical Thinking', "Are you unsure about statistics?  Perhaps you haven't done them before, you need a recap, or you're truly terrified!", 'Mon, 11 Feb 2019 11:00:00 ', 'Mon, 11 Feb 2019 12:00:00', 'Liverpool Campus, Sydney Jones Library, KnowHow Space'], ['KnowHow Academic English: Critical Thinking', 'Are you wondering how you can be more critical in your studies?  Come join our Critical Thinking sessions to discover how you can develop both your ability to be critical and the language to express criticality in your work.', 'Mon, 11 Feb 2019 12:00:00 ', 'Mon, 11 Feb 2019 13:00:00', 'Liverpool Campus, Sydney Jones Library, KnowHow Space'], ['KnowHow Academic English: Writing at University', 'Are you wondering how you can be more critical in your studies?  Come join our Critical Thinking sessions to discover how you can develop both your ability to be critical and the language to express criticality in your work.', 'Mon, 11 Feb 2019 12:00:00 ', 'Mon, 11 Feb 2019 13:00:00', 'Liverpool Campus, Sydney Jones Library, KnowHow Space'], ['Career Lounge with Chatteris Educational Foundation', 'Would you like to develop your Academic Writing skills so you can express yourself clearly? Come join our Writing at University sessions.', 'Mon, 11 Feb 2019 13:00:00 ', 'Mon, 11 Feb 2019 14:00:00', 'Liverpool Campus, 1-7 Abercromby Square, G37'], ['KnowHow - Planning Your Essay', 'Apply to the Chatteris Educational Foundation for the opportunity to join a graduate programme based in Hong Kong!', 'Mon, 11 Feb 2019 14:00:00 ', 'Mon, 11 Feb 2019 15:00:00', 'Liverpool Campus, Career Studio, Alsop Building, Connect Zone'], ['PwC Presentation: Artificial Intelligence in Audit - The Future of AI', 'Learning how to plan and structure an essay is an essential part of academic writing, and this workshop will increase your confidence in working through the process.', 'Mon, 11 Feb 2019 14:00:00 ', 'Mon, 11 Feb 2019 15:00:00', 'Liverpool Campus, Sydney Jones Library, KnowHow Space'], ['KnowHow Academic English: Listening', 'Artificial Intelligence in Audit - The Future of AI', 'Mon, 11 Feb 2019 17:30:00 ', 'Mon, 11 Feb 2019 19:30:00', 'PwC Manchester Office, 1 Hardman Square, M3 3EB'], ['ool Campus, Gordon Stephenson\xa0Building, Seminar Room G33</venue></item></channel></rss></body></html', 'The course aims to develop your listening skills to help you achieve your full potential on your main programme.', 'Tue, 12 Feb 2019 09:00:00 ', 'Tue, 12 Feb 2019 10:00:00', 'Liverpool Campus, Gordon Stephenson\xa0Building, Seminar Room G33']]

for out in output:
    print(out[0])
    print(out[1])
    print()