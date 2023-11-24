import json
import numpy

fs = open("textfiles/hello.txt", 'r')
fd = fs.read()
statement_embeddings = json.loads(fd)
questions_embeddings = numpy.array(statement_embeddings)


answers = ["A news title is a succinct summary of an article, placed at the top to capture attention and provide a brief overview of the topic. It is designed to give readers a glimpse into the article's content and entice them to read further. On the other hand, a statement is a more detailed and informative sentence or collection of sentences within the article itself. Statements convey specific information, viewpoints, or claims related to the topic, offering depth and context to the overall narrative. While news titles are concise and serve as attention-grabbers, statements provide substance and contribute to the article's content by presenting detailed information or supporting arguments.", "Users are prompted to crop the image to select the specific portion of text they want to use as input. If the image contains multiple text statements, users can choose the desired section by cropping the image accordingly.","Real news refers to factual and accurate information that is based on verified facts, evidence, and reliable sources. It undergoes rigorous journalistic processes, such as fact-checking and verification, to ensure its credibility. Real news aims to provide unbiased and objective reporting of events, issues, and developments, adhering to ethical journalistic standards. On the other hand, fake news refers to deliberately fabricated or misleading information presented as news. It can be created to deceive, manipulate, or spread false narratives. Fake news lacks factual basis, often containing misinformation, biased viewpoints, or outright falsehoods. Its purpose may be to generate clicks, manipulate public opinion, or promote specific agendas. Differentiating between real news and fake news requires critical thinking, fact-checking, and reliance on trusted sources.","Grammatical check refers to the process of examining the given input for spelling mistakes and ensuring proper grammar usage. The input must successfully pass the grammatical check before proceeding to subsequent checks.","""The process of grammatical check involves breaking down the given input into individual words and then using the Python GINGERIT library to check the spelling of each word. To calculate the spelling mistake ratio, the number of misspelled words in the input text is divided by the total number of words in the input text using the following formula:
ratio = Number of misspelled words in the given input text / Total number of words in the given input text
If the calculated ratio exceeds 0.6 (approximately), it indicates a high proportion of spelling mistakes, and the input text is considered fake news. In such cases, the input fails the grammatical check and will not proceed to the subsequent checks.
On the other hand, if the ratio is below 0.6, the input text passes the grammatical check and can proceed to the subsequent checks.""","Real news articles generally exhibit a higher level of grammatical accuracy due to the rigorous editorial processes they undergo. While occasional minor errors may occur, they are typically unintentional and do not significantly impact the overall quality. In contrast, fake news articles often lack the same level of scrutiny and may contain more noticeable grammatical mistakes. These errors can arise from hasty production, lack of professionalism, or intentional attempts to mimic informal language. However, it is important to note that relying solely on grammatical mistakes to determine the authenticity of news is inadequate, as thorough fact-checking and source verification are essential for a comprehensive assessment.","It is crucial to understand that the presence or absence of grammatical mistakes alone is not a reliable indicator of the authenticity of a news article. Assessing the credibility of news requires a comprehensive evaluation that involves multiple factors, including source reliability, evidence, corroboration, and fact-checking from reputable sources.","After successfully passing the grammatical check, the given input proceeds to undergo subsequent checks.","clickbait check refers to the process of examining the given input text wheather it is clickbait title or not. The input must successfully pass the clickbait check before proceeding to subsequent checks.","In the clickbait analysis, the input text is fed into a Random Forest Classifier machine learning model. This model has been trained on a pre-existing dataset comprising both clickbait and non-clickbait sentences. Based on the input text, the model predicts whether it falls into the category of clickbait or not. If the model predicts that the input text is clickbait, it indicates that the text has failed the clickbait test and will not proceed to further checks. On the other hand, if the model predicts that the input text is non-clickbait, it signifies that the text will proceed to the subsequent checks.","Real news articles generally aim to provide informative and objective headlines, avoiding excessive sensationalism or exaggeration. Clickbait titles are more commonly associated with fake news, as they employ attention-grabbing tactics to lure readers and generate clicks. Fake news often utilizes exaggerated, misleading, or sensationalized clickbait titles that may misrepresent the actual content of the article. In contrast, real news titles prioritize accuracy, clarity, and adherence to journalistic standards, aiming to provide an honest representation of the news story without resorting to manipulative or deceptive clickbait techniques.","clickbait check alone cannot determine the authenticity of a news article. While clickbait analysis helps identify attention-grabbing or sensational titles, it does not provide direct evidence of the article's veracity. Assessing the truthfulness of news requires a comprehensive evaluation that includes fact-checking, source verification, cross-referencing, and critical analysis of the content. Clickbait titles can be used in both real and fake news articles, and relying solely on clickbait analysis would not provide a conclusive assessment of the article's authenticity","After successfully passing the clickbait check, the given input proceeds to undergo subsequent checks.","Subjectivity check involves analyzing the given input text to determine whether it contains a subjective or objective statement. Only objective statements are accepted, and the input must pass the clickbait check before proceeding to further evaluations.","The Subjectivity analysis involves inputting the text into a Google transformers BERT deep learning machine model. This model has been trained on a pre-existing dataset containing a mix of subjective and objective sentences. Using the input text, the model predicts whether the text is a subjective statement or an objective statement.","Real news articles typically aim to present information objectively and impartially, resulting in objective titles that state the facts without personal bias. Subjectivity in news titles is more commonly associated with fake news, as they may employ sensational or opinionated language to manipulate readers' emotions or skew the narrative. Fake news titles often exhibit a higher degree of subjectivity, promoting a specific agenda or viewpoint rather than providing balanced and factual reporting. In contrast, real news titles prioritize neutrality, accuracy, and adherence to journalistic principles, avoiding subjective language that may distort the objective representation of the news story.","Subjectivity check alone cannot determine the authenticity of a news article. While subjectivity analysis helps identify whether a statement is subjective or objective, it does not provide direct evidence of the article's veracity. Assessing the truthfulness of news requires a comprehensive evaluation that includes fact-checking, source verification, cross-referencing, and critical analysis of the content. Subjectivity can be present in both real and fake news articles, and relying solely on subjectivity analysis would not provide a conclusive assessment of the article's authenticity.","After successfully passing the clickbait check, the given input proceeds to undergo subsequent checks.","The News Title check entails examining the given input text to ascertain whether it represents a news title or a statement. Only text that qualifies as a news title will be accepted, and the input must successfully pass the News Title check before proceeding to subsequent evaluations.","The News Title analysis utilizes a Naive Bayes Classifier machine learning model to process the input text. This model has been trained on a dataset comprising a combination of News titles and regular statements. By inputting the text, the model makes a prediction on whether it represents a News title or a statement.","fake news articles often utilize normal sentences as titles, which may not explicitly indicate their newsworthiness or the main topic of the article. These titles might resemble regular statements rather than traditional news headlines. On the other hand, real news articles typically employ actual news titles that follow conventional journalistic practices. These titles are specifically crafted to summarize the main point or subject matter of the news article, giving readers a clear indication of the news content. Real news titles aim to convey the essence of the story in a concise and informative manner, allowing readers to quickly grasp the topic and make an informed decision on whether to read further.","While the difference between news titles and sentences can provide some indication, it is not sufficient on its own to classify real and fake news reliably. While fake news articles may sometimes use regular sentences as titles, there can also be real news articles with informative sentences as titles. Therefore, relying solely on this distinction would not be a comprehensive approach to classify news articles. Assessing the authenticity of news requires additional factors such as source credibility, fact-checking, corroboration, and critical analysis of the content. It is essential to consider multiple criteria and employ a thorough evaluation process to make a more accurate determination between real and fake news.","While we have a high level of confidence in our predictions, we cannot guarantee with absolute certainty whether the given input is real or fake. Our website relies on reputable news sources and the availability of information on the internet as key criteria for analysis. However, we advise users to exercise caution and use our predictions at their own discretion. We hold no responsibility for any actions taken by users based on our website's predictions.","While we have a high level of confidence in our predictions, we cannot guarantee with absolute certainty whether the given input is real or fake. Our website relies on reputable news sources and the availability of information on the internet as key criteria for analysis. However, we advise users to exercise caution and use our predictions at their own discretion. We hold no responsibility for any actions taken by users based on our website's predictions.","To identify real news, consider the following tips: First, verify the source by checking its credibility and reputation. Second, cross-reference multiple sources to ensure consistency and reliability. Third, check the author's credentials and look for expertise in the subject matter. Fourth, look for unbiased reporting that presents multiple perspectives. Fifth, examine the evidence and sources cited to ensure credibility. Sixth, fact-check the information using reputable fact-checking sources. Seventh, evaluate the tone and language of the article for professionalism and lack of extreme bias. Finally, be critical and skeptical, questioning information that appears too good or bad to be true. By employing these tips, you can increase your ability to identify real news.","While we have a high level of confidence in our predictions, we cannot guarantee with absolute certainty whether the given input is real or fake. Our website relies on reputable news sources and the availability of information on the internet as key criteria for analysis. However, we advise users to exercise caution and use our predictions at their own discretion. We hold no responsibility for any actions taken by users based on our website's predictions.","After the text input successfully passes all the checks, we proceed to verify its availability on the internet, primarily through search engines like Google, focusing on news articles. We examine the number of articles containing the input text that exist on the internet. A higher number of articles suggests that the text is circulating and likely represents a genuine news story. Conversely, a limited number of articles indicates the text is not widely present on the web, lacking supporting articles that would corroborate its authenticity.","Hello, I'm REGA! Your friendly and interactive assistant here to provide assistance with any queries you may have about our website. Don't hesitate to ask me any questions or doubts you may have. I'm here to help and I'll do my best to put a smile on your face while providing the information you need!", "Fake news refers to intentionally fabricated or misleading information presented as news, often spread through various media channels. It aims to deceive or manipulate readers by distorting facts, spreading false narratives, or promoting biased viewpoints. Fake news can be created for various reasons, including political propaganda, financial gain, or simply to generate attention and engagement. It poses a significant threat to public discourse, as it can influence opinions, undermine trust in legitimate news sources, and contribute to the spread of misinformation and societal division. Combatting fake news requires critical thinking, fact-checking, and reliance on trusted sources of information.",
"Real news refers to accurate, reliable, and fact-based information that is thoroughly researched, verified, and reported by professional journalists and news organizations. It is based on a commitment to journalistic principles such as objectivity, fairness, and transparency. Real news aims to inform the public about current events, issues, and developments in an unbiased and responsible manner. It undergoes editorial processes that involve multiple layers of fact-checking, source verification, and ethical considerations. Real news plays a vital role in a democratic society, enabling citizens to make informed decisions, holding those in power accountable, and fostering an informed and engaged public.",
"The main difference between fake news and real news lies in their credibility and accuracy. Fake news is intentionally fabricated or misleading information presented as news, often with the aim of deceiving or manipulating readers. Real news, on the other hand, is accurate, fact-based, and reported by professional journalists and news organizations following journalistic standards and practices. Fake news is created to spread false narratives and generate attention, while real news is meant to inform the public and foster an informed citizenry. Distinguishing between fake news and real news requires critical thinking, fact-checking, and reliance on trusted sources.",
"Hello! Feel free to ask me anything, whether it's for educational purposes, seeking advice, or simply engaging in a conversation. I'll do my best to assist you!",
"You're welcome! If you have any more questions or need further assistance, feel free to ask. I'm here to help!",
"The project's accuracy is significantly enhanced by leveraging deep learning and machine learning techniques, as well as utilizing APIs and incorporating the use of Random Forest. To further improve accuracy, additional checks have been implemented to filter out statements and only accept news. Consider the following example: If the news states 'Modi is visiting Chennai', it would be classified as true news. Similarly, if the input is 'Modi is visiting India,' it would also be considered true news since Chennai is a part of India. However, if the input is 'Modi is visiting Gujarat,' it would be classified as false news as Gujarat is a different state. To verify the accuracy, you can test the system with various news samples.",
"The primary objective of this website is to detect the authenticity of news, distinguishing between true and fake information. By doing so, it aims to mitigate the detrimental effects and confusion caused by the dissemination of fake news, which can be harmful to society. To achieve this, the website employs automated mechanisms to populate and analyze news content, reducing the impact of fake news and promoting reliable information.",
"Initially, we utilize a Random Forest model in machine learning to predict the output. Subsequently, we conduct a series of checks on the search query, including determining if it is clickbait, a statement, subjective, or contains any grammatical errors. If it successfully passes all these checks, we proceed to the web scraping stage where the search query is analyzed using natural language processing (NLP) to identify similarities. The analysis is performed on the most similar model selected based on the maximum similarity score. Afterward,we check whether it is present in news and utilizing the integration with OpenAI, we determine whether the news is true or fake. Finally, upon completing the entire process, we locate the email of the deceptive user and automatically send them the original news.",
"Initially, we offer users two options: user-generated input or input extracted from the heading of a news article. If the input is user-generated, we only perform two checks: subjectivity/objectivity and grammatical correctness. However, if the input is extracted from a news website heading, we conduct four checks, including clickbait identification and differentiation between news and statements. In the case of users providing an image of the news, we extract the text from the image and apply the same two checks as in user-generated input.",
"Clickbait refers to a deceptive or sensationalist technique used in online content to entice users to click on a link. It typically involves the use of exaggerated or misleading headlines, thumbnails, or descriptions that create curiosity or shock value. The primary objective of clickbait is to generate high click-through rates and increase website traffic, often at the expense of accurate information or user experience. Clickbait often promises extraordinary or unbelievable content but fails to deliver on its claims, leaving users disappointed. It is widely used in various forms of online media, including news articles, social media posts, and video thumbnails, with the intention of maximizing views and engagement.",
"""we have three check boxes
->one is it is user generated news
->one is it is news picked up from the news heading
->other is whether the checkbox has indian places and names""",
"The first checkbox presents two options, distinguishing between user-generated input and other types. In the case of user-generated content, only two checks are performed: subjectivity and grammar. However, if the user clicks on a news article heading, an additional set of four checks is initiated. These checks include verifying grammatical correctness, assessing subjectivity versus objectivity, determining if the content is news or a statement, and evaluating whether it falls under the category of clickbait or not. Therefore, the number of checks varies depending on the type of input and user interaction.",
"The second checkbox pertains to determining whether the user's input contains more Indian place names or not. Since Indian names are not typically recognized as correct in standard English dictionaries, we exclude the check for grammatical correctness from our evaluation. Instead, we focus solely on the presence or absence of Indian place names in the user's input. This criterion helps us analyze the content in terms of its relevance to Indian locations, allowing for a more specific assessment. By emphasizing Indian place names, we can ensure that the evaluation aligns with the context and preferences of the target audience.",
"Subjectivity refers to the personal opinions, feelings, perspectives, or biases that influence an individual's interpretation or judgment of a particular topic or situation. It is the opposite of objectivity, which aims to present information or analysis based solely on facts and without personal biases. Subjectivity often involves an individual's emotions, beliefs, values, and experiences, which can shape their understanding and evaluation of events, ideas, or arguments. When assessing subjectivity, one examines the extent to which a statement or piece of content is influenced by personal viewpoints, emotions, or subjective interpretations, as opposed to being based purely on verifiable facts or objective criteria.",
"Objectivity refers to an approach that emphasizes factual accuracy and impartiality in presenting information or making judgments. It involves a detachment from personal biases, emotions, and subjective interpretations, focusing instead on presenting information based on observable evidence and universally accepted standards. Objectivity aims to provide a fair and unbiased representation of reality, considering multiple perspectives and avoiding undue influence from personal opinions or preferences. It is an important principle in journalism, scientific research, and critical analysis, as it ensures transparency and credibility in the communication of information. Objectivity enables a more objective understanding of events, issues, and arguments, fostering rational decision-making and informed discourse.",
"Subjectivity refers to personal opinions, biases, and interpretations, influenced by individual perspectives and emotions. Objectivity, on the other hand, focuses on presenting information based on facts and observable evidence, free from personal biases. Subjectivity is subjective and varies from person to person, while objectivity strives to be universally applicable and impartial. Objectivity emphasizes fairness, accuracy, and detachment from personal viewpoints, whereas subjectivity incorporates personal experiences and judgments.",
"To address the issue of the news potentially containing numerous Indian words without adding any meaningful value, please click on the checkbox indicating the presence of multiple Indian words in the input. If you have any additional concerns or questions, please feel free to ask.",
"To mitigate the issue of receiving statements as input, which could potentially be subjective, grammatically incorrect, or overly generalized, consider selecting the checkbox for user-generated messages or opting for image upload. If the content is still identified as a statement despite these measures, it is highly likely to be a genuine statement.",
"The most dependable verification method is the news_title_check, which utilizes a robust machine learning model trained on an extensive dataset. This model excels at categorizing content as either news or statements, employing the Naive Bayes algorithm. The utilization of this powerful machine learning technique enhances the reliability of the classification process, allowing for accurate identification of news articles. By leveraging a vast amount of data and employing sophisticated algorithms, the news_title_check plays a crucial role in distinguishing between factual news and other forms of content.",
"""Verify the source: Check the credibility and reputation of the news source by researching its background, editorial standards, and fact-checking practices. Trusted and established news organizations are generally more reliable.
Cross-reference information: Look for multiple sources reporting on the same news story. Compare different perspectives and sources to get a more balanced understanding of the topic.
Evaluate the content: Scrutinize the content for signs of sensationalism, extreme bias, or emotionally charged language. Misleading headlines, lack of verifiable sources, or exaggerated claims are red flags to watch out for.
Fact-check with reliable sources: Use fact-checking websites or trusted sources to verify the accuracy of the information presented. Fact-checkers provide independent assessments of claims and can help identify misinformation.
Be critical and think critically: Develop a healthy skepticism and think critically before accepting or sharing news. Consider the motives behind the news, look for supporting evidence, and question the reliability of the information before drawing conclusions or spreading it further.""",
"A statement can be considered clickbait when it employs sensational or exaggerated language with the intention of enticing users to click on the content. Clickbait statements often make bold claims or promises that are not fulfilled or adequately supported within the actual content. They are designed to generate curiosity, engagement, and high click-through rates without necessarily providing valuable or meaningful information. Clickbait statements aim to capture attention and drive traffic rather than delivering substantive content or fulfilling the expectations set by the headline or preview.", "While we have a high level of confidence in our predictions, we cannot guarantee with absolute certainty whether the given input is real or fake. Our website relies on reputable news sources and the availability of information on the internet as key criteria for analysis. However, we advise users to exercise caution and use our predictions at their own discretion. We hold no responsibility for any actions taken by users based on our website's predictions.","""The primary objective of this project is to counter the proliferation of false information by automatically generating authentic news articles on websites that propagate fake news. By doing so, we aim to minimize the dissemination of misleading content and offer users reliable and accurate information""", "We employ a Python library called Easy OCR as our tool for Optical Character Recognition (OCR). Using this tool, we extract text from various sources and apply the same procedures employed in text analysis", "By utilizing the Beautiful Soup library, we scrape the user-provided input and extract relevant information. Subsequently, we leverage OpenAI embeddings to determine the similarity between the extracted results and other data.","""False news: This is news that is completely made up.
Misleading news: This is news that is technically true, but it is presented in a way that is misleading.
Satire: This is news that is intended to be funny, but it is often mistaken for real news.
Propaganda: This is news that is used to promote a particular viewpoint or agenda""", """Fake news can be created by anyone, but it is often created by people who want to make money or to influence public opinion. There are a number of ways to create fake news, including:Fabricating stories: This involves making up stories from scratch.
Taking real stories and changing them: This involves taking real stories and changing them to make them false or misleading.
Sharing false or misleading information: This involves sharing information that you know or believe to be false or misleading.""", """Social media: Social media is a major platform for spreading fake news. This is because fake news can be easily shared on social media, and it can reach a large number of people quickly.
Email: Email is another common way to spread fake news. This is because emails are often trusted, and people are more likely to believe information that they receive in an email.
Websites: Fake news can also be spread through websites. This is because websites can be designed to look like legitimate news websites, and people may not realize that they are reading fake news.""","""Influencing public opinion: Fake news can be used to influence public opinion on a variety of issues. This can have a significant impact on elections, policy decisions, and other important matters.
Damageing trust in institutions: Fake news can damage trust in institutions, such as the media and government. This can make it difficult for people to get accurate information and to make informed decisions.
Promoting violence: Fake news can be used to promote violence or other harmful behavior. This is especially true in the context of conflict or political unrest."""]
questions = ['what is the difference between news title and statement?', 'What is the purpose of cropping the image during the upload process?', 'What is the difference between real and fake news?', 'What is grammatical check?', 'how does grammatical check work?', 'how can grammatical check determine whether a news article is fake or real?', 'can grammatical check alone determine whether a news article is fake or real?', 'what happens after the given input passes the grammatical check?', 'what is clickbait check?', 'how does clickbait check work?', 'how can clickbait check determine whether a news article is fake or real?', 'can clickbait check alone determine whether a news article is fake or real?', 'what happens after the given input passes the clickbait check?', 'what is Subjectivity check?', 'how does Subjectivity check work?', 'how can Subjectivity check determine whether a news article is fake or real?', 'can Subjectivity check alone determine whether a news article is fake or real?', 'what happens after the given input passes the Subjectivity check?', 'What is News Title check?', 'how does News Title check work?', 'how can News Title check determine whether a news article is fake or real?', 'can News Title check alone determine whether a news article is fake or real?', 'How can you justify your classfication of real and fake news?', 'Can i trust the website prediction of the text?', 'Do you have any tips to identify real news?', 'Describe the accuracy of your website?', 'what happens after the text input passes all the checks?', 'Who are you?', 'what is fake news?', 'what is real news?', 'what is difference between fake news and real news?', 'hi', 'Thank you', 'describe the accuracy of your website', 'what is the purpose of this website', 'how does this website identify news is fake or not?', 'what are these inputs conveying?', 'what is clickbait?', 'explain about check boxes in this website', 'what is first check box explaining?', 'what is second check box explaining?', 'what is subjectivity?', 'what is objectivity?', 'what is difference between subjectivity and objectivity?', 'why I am getting my input as grammatically mistake?', 'why I am getting input as statement?', 'which is the most important check in this website?', 'do you have any tips for identifying fake news in real life ?', 'why I am getting my input as click bait?', 'Can I trust your website',"what is autopopulation in this website?","what is the tool which you are using to extract text from image?","how do you analyse the input given by user?","What are the different types of fake news?","How is fake news created?","How is fake news spread?","What are the effects of fake news?"]