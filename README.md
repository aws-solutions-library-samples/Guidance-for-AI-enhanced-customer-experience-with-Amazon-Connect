# Guidance for AI enhanced customer experience with Amazon Connect

## Introduction
This Guidance demonstrates how Amazon Connect can revolutionize your customer experience using Amazon Connect AI-powered automation and agent assistance. By implementing this solution, businesses can deliver 24/7 omnichannel support while significantly improving operational efficiency and customer experience. The integration enables natural, conversational customer interactions through generative AI, seamless escalation to human agents when needed, and empowers customer service representatives with real-time AI assistance. This AI-powered approach to customer service helps organizations reduce improve customer satisfaction, increase business growth, while optimizing operational costs and enabling support teams to focus on high-value interactions.

Deploy intelligent, ai-conversational support that services customer inquiries without human-agent intervention. Amazon Q in Connect leverages large language models to provide contextual responses from your knowledge base, improving customer self-service success rates.

Enable seamless transitions from AI-powered self-service to human agents when needed. Customers maintain context as they move between chat, voice, video, or in-app channels, creating a cohesive support experience that improves customer experience.

Automate and self-serve routine inquiries while directing complex issues to human agents. This approach, improves customer experience, reduces wait times, allows agents to focus on high-value interactions, and captures complete interaction history for continuous improvement of both AI and human-assisted support.

 
## Architecture overview
The architecture for this Amazon Connect solution consists of the following key components: 
1.	[Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/connect-feature-overview.html) - The core service providing Contact Centre capabilities to interact with customers
2.	[Amazon Q in Connect](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-q-connect.html) - The core service providing the generative AI capabilities to answer questions based on the enterprise data
3.	[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Storage capability to house documentation accessed by Amazon Q and host a static webpage.
4.	[CloudFront](https://aws.amazon.com/cloudfront/) – A Content Distribution Network capability to present customer facing website.

NOTE: The solution is designed to be deployed in regions where Amazon Connect and Amazon Q services are available. Please verify service availability in your preferred region before deployment. https://docs.aws.amazon.com/connect/latest/adminguide/regions.html 

 ![image](images/9.jpeg)

## Cost
This bundle uses the following resources:

### Amazon Connect
Amazon Connect provides unlimited use of AI capabilities that power end-customer self-service, agent assistance, and supervisor experiences. It allows you to optimize every step of your customer journey without cost-driven compromises. Learn more [here](https://aws.amazon.com/connect/pricing/). Alternatively, you can continue buying Amazon Connect features [individually](https://aws.amazon.com/connect/pricing/#Amazon_Connect_with_individual_features). 

You are responsible for the cost of the AWS services used while running this Guidance. The cost for running this Guidance with the default settings in the US East (N. Virginia) with unlimited AI is approximately $5,300 per month for 100,000 minutes of in-app calls and 50,000 chat messages per month with all calls analyzed to provide Conversational analytics & post contact summaries.  This guidance scenario also includes automated performance evaluations for 75 contact center agents.

The following table provides a sample cost breakdown for deploying this Guidance with the default parameters in the US East (N. Virginia) Region for one month.

| Channels | Conversational analytics & post-contact summaries | Screen Recording | Real-time agent assistance | End-customer self-service | Automated performance evaluations | Agent forecasting & scheduling | Pricing |
|-----------|------------|------------|------------|------------|------------|------------|------------|
| Voice (telephony, in-app and web, video)| X |  | X | X | X| | $0.048 per min (see note 1) | 
| Chat | X |  | X | X | X| | $0.010 per message | 

Notes:
1. For Amazon Connect Voice, there are two charges associated with usage: voice service AI charges and a charge for the communication service i.e. in-app and web calling. In this chart, the voice service AI charge is $0.038, and you are separately charged for the in-app and web calling audio communication at a rate of $0.010 per minute, resulting in a charge of $0.048 per minute.
 Pricing example:
* Omnichannel Customer Service: Let’s assume your 75-agent contact center receives 100,000 voice minutes, and 50,000 chat messages per month. You want to enable conversational analytics, real-time agent-assist, and end-customer self-service chatbots:
*    There is an Amazon Connect voice usage charge, based on end-customer call duration. At $0.038 per minute * 100,000 minutes = $3,800.
*   The per minute in-app voice usage charge at $0.010 per minute * 100,000 minutes = $1,000. 
*   There is an Amazon Connect chat usage charge, based on the total messages sent during the chat (including initial message when chat was started). At $0.01 per message * 50,000 chat messages = $500 per month.
*   The monthly cost is $5,300 [plus applicable taxes, fees, and surcharges](https://aws.amazon.com/tax-help/telecommunications-services/). 


You are responsible for the cost of the AWS services used while running this Guidance. The cost for running this Guidance with the default settings in the US East (N. Virginia) with unlimited AI is approximately $5,300 per month for 100,000 minutes of in-app calls and 50,000 chat messages per month with all calls analyzed to provide Conversational analytics & post contact summaries.  This guidance scenario also includes automated performance evaluations for 75 contact center agents.
The following table provides a sample cost breakdown for deploying this Guidance with the default parameters in the US East (N. Virginia) Region for one month.


## Customer Journey
1. User navigates to a webpage hosted on Amazon S3 and distributed via AWS CloudFront. 
2. End-User or Customer interacts using a chat widget on the webpage.
3. When users interact with the chat widget, a Contact Flow is triggered which invokes the use of Amazon Q in Connect and Lex.
4. Amazon Q in Connect proactively engages with the customer during the interaction using the integrated knowledge base and to provide real-time responses
5. If the customer requests to speak with a human agent, the users have a click to call button for a seamless transfer to an available agent.

## Technical prerequisites
To deploy this solution, you will need an AWS Administrator Account with “AdministratorAccess” AWS managed.


### Assumptions

1.	You have an active Amazon Web Services (AWS) account with the necessary permissions to provision the required resources.
2.	You have a basic understanding of AWS services
3.	You have the ability to create and manage Identity and Access Management (IAM) Identity Centre users and assign the necessary permissions.
4.	You have prepared Knowledge Base Content - FAQ documentation in supported formats (PDF, DOC, DOCX) for upload to Amazon Q


 
## Deployment guide
The deployment process consists of several key steps that must be performed in order. Follow each section carefully to ensure proper configuration.


### CloudFormation Deployment
1.	Download CloudFormation template 'smb-builder.yaml'
2.	Login to your AWS account, select your preferred region.  Note: Amazon Connect is available in select regions.  Refer to documentation for the latest available regions: https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#amazonconnect_region  
3.	Navigate to CloudFormation.
4.	Select Create Stack > With new resources (standard) >Choose an existing template > Upload a template file > Choose file.
5.	Select the downloaded .yaml file > Next.
6.	Complete Stack details:
    - Enter a stack name of your choice.
    - AdminPassword (you can change this to a password of your choice, if you leave it as is, the password will be Admin123!.  Passwords must contain at least 8 characters with an uppercase letter, a      lowercase letter, and a number)
    - AdminUsername (Username for the Connect admin user)
    - FAQBucketName – Enter a name of your choice.  This is the S3 bucket where your FAQ documents will be stored.
    - InstanceAlias – Enter a name of your choice. This will be the Amazon Connect Instance Name
    - S3BucketName – Enter a name of your choice. This will be the bucket used to store the static website
  
7.	Click Next
   
 	 ![image](images/10.jpeg)

8.	Leave all selections as default and scroll down to Capabilities and select ‘I acknowledge that AWS CloudFormation might create IAM resources.’
9.	Click Next
10.	Leave all sections as is, scroll down to bottom of page and select Submit.
 	Your CloudFormation template will start deploying with status ‘CREATE_IN_PROGRESS.  This build process will take a 10-15minutes to deploy.
11.	When the CloudFormation is ‘CREATE_COMPLETE’ navigate to the Outputs tab and note down the FAQBucket, and S3Bucket names and the WebsiteURL.

### Set up Amazon Q Knowledge Base

1.	In the menu bar of the console, type in Amazon Connect and click Amazon Connect from the Services menu to navigate to the Amazon Connect AWS console.
2.	In the Amazon Connect console, click on the Instance alias name that was created during the deployment.
3.	In the left-hand menu, select Amazon Q.

 ![image](images/11.jpeg)

4.	Select Add Domain > Create a new domain.  Enter a preferred domain name like “my-q-in-connect”.
5.	Select Create an AWS KMS Key. This will navigate to the Customer-managed keys page of the Key Management Service (KMS) console.  
6.	In the KMS console, on the Configure key page:  
    - Choose Key Type - Symmetric.  
    - Key Usage – Encrypt and decrypt.  
    - Click Next.

    ![image](images/12.jpeg) 

    - On the Add labels page, enter a display name for your key in the Alias field and click Next.
    - On the Define key administrative permissions page, leave everything default and click Next.
    - On the Define key usage permissions page, leave everything default and click Next.
    - On the Edit key policy page.  Use the toggle button on the right-hand corner and move to ‘Edit’.
    - Copy and paste the updated key policy configuration below into the key policy.  Note; make sure you include your account number in the configuration before pasting into the Key policy
  
    ![image](images/18.jpeg) 

    - When the policy has been updated, click Next
    - On the Review page scroll to the bottom of the page then click Finish

7.	Return to the AWS Amazon Connect console and the Amazon Q Add domain page.  Select the new KMS Key.  Click Add domain.
8.	On the same Amazon Q page, click on ‘Add integration’

![image](images/14.jpeg) 

9.	On the Add integration page, choose Create a new integration, and under Source select S3.
10.	Add an integration name of your choice.
11.	Under Connection with S3, click the Browse S3 button and search the bucket name created in previous CloudFormation step 6.c (FAQBucket). Select bucket and click choose.

![image](images/15.jpeg) 
  
12.	In the Encryption section, select the KMS Key you created previously.  
13.	Click: Next > Add integration
14.	browse to the Cloudformation Outputs tab and locate the S3 bucket create for FAQBucketName
    ![image](images/27.jpeg)
15. Browse to the S3 bucket and inside should be a file called FAQ.docx
16. Download the file and re-upload it to the bucket. Don't change anything, this is to trigger a sync to QiC integeration just created.


### Enable Lex Bot
1.	Navigate back to the Amazon Connect console and the new instance name.
2.	On the left-hand menu, at the bottom, click ‘Flows’
3.	Check both boxes under Amazon Lext Bots and click ‘Save’.  This provides the ability for the Lex bot to be created in the Amazon Connect Admin Console.

![image](images/17.jpeg) 


### Enable Recording
1.	Navigate back to the Amazon Connect console and the new instance name.
2.	On the left-hand menu, at the bottom, click ‘Data Storage’.
3.	Select Edit on Call recordings.
4.	Select Enable call recording > Create a new S3 bucket (recommended)> name > Save.
![image](images/28.jpeg)

### Chat transcripts
1.	Navigate back to the Amazon Connect console and the new instance name.
2.	On the left-hand menu, at the bottom, click ‘Data Stroge’.
3.	Select Edit on Chat transcripts.
4.	Select Enable chat transcripts > Create a new S3 bucket (recommended) > name > Save.
![image](images/29.jpeg)
5.	Navigate back to the Overview section of your Amazon Connect Instance by clicking the Instance Name in the top left corner.
6.	In the Access Information of the Account Overview, click on the Access URL link.
7.	This will take you to the Amazon Connect Admin console, use your username and password you entered when deploying your stack.  The default was username; Admin, Password, Admin123!
   
### Configure Lex Bot
1.	On the left-hand menu of the admin page, navigate to Routing > Flows > bots.
2.	Select Create Bot > call the bot “MenuBot”, leave the Children’s Online Privacy Protection Act (COPPA) as default setting > Click Create.
3.	Select Add language > English (US).
4.	In the Amazon Q in Connect intent section, Enable Amazon Q in Connect Intent.
![image](images/1.jpeg) 
5.	In the Enable Amazon Q in Connect intent pop-up window, select your bot from the drop down.  The bot’s name will start with arn:aws:wisdom.  Click Confirm.
![image](images/2.jpeg) 
6.	Click Build language

### Configure Contact Flow

1.	From Amazon Connect UI navigate to Routing > Flows.
2.	Select the -inboindFlow-_20250508_222550
3.	When the contact flow is opened, follow the instructions of the Note cards to update the flow blocks.
4.	Click Publish in the top right of the screen, you will see a ‘Flow published successfully!’ message in the top left of the screen confirming the change is complete.


### Configure Chat Widget

1.	From Amazon Connect UI navigate to Channels > Communication widgets > Add widget


2.	Add the following details:
    - Name: Enter a name of your choice
    - In the Chat contact flow, select the -inboindFlow-_20250508_222550 flow from the drop down.
    - Select the same flow for the Web calling contact flow
    - Click Save and continue
    ![image](images/5.jpeg) 

    
3.	On the Customise widget page, update the Define widget access button styles as follows:
    - Start chat icon background color: 0f1e5a
    - Icon Color – Leave White
    - Minimize chat icon background color: 0f1e5a
    - Icon Color - White

4.	Update the Widget Header with the following changes:
    - Header message, change to: 24/7 Support
    - Change Header color to: 0f1e5a
    - Leave widget background color as default: ffffff
    - Leave the Logo URL blank


5.	In the Chat view section, make the following changes:
    - Change the Typeface to Tahoma
    - In the System Message Display Name, hit the space bar (this removes the System Message)
    - In the Bot Message Display Name, hit the space bar (this removes the System Message)
    - IN the Text Input Placeholder, hit the space bar (this removes the System Message)
    - Change the Agent chat bubble color, to 6fa3d9
    - Change the Customer chat bubble color to bd9a62


    - Click Save and continue

6.	In the Domain & Security section make the following changes:
    - In the Add the required domains for the communication widget.  Paste the URL copied from the WebsiteURL CloudFormation stack
  
![image](images/19.jpeg) 

    - In the Add security for new communication widget requests, change the Would you prefer to do this? To ‘No’
    - Click Save and continue


7.	On the final review page, select ‘Copy Script’.  This will copy the Widget Script.



### Configure Webpage 

1.	Login to your AWS account and navigate to S3.
2.	Search for the S3Bucket name noted down in step 11 Section CloudFormation Deployment.
3.	From the root folder, select the index.html file and click download.  
4.	Open the file using a text editor like Visual Code, delete lines 27 – 39.
5.	Paste the Widget script into the same file starting at line 27

![image](images/7.jpeg) 

6.	Save the file as index.html to your local machine
7.	Navigate back to the S3 bucket and add to new file updated file to the bucket.
8.	Click Upload.  This will overwrite the existing .html file


### Test your new self-service solution
You can access the deployed solution through the static webpage hosted on CloudFront.  
1.	Navigate to CloudFormation in the AWS Console.
2.	Select the stack name you created in step 3 of the Deployment Guide, CloudFormation section.
3.	Click on the Outputs tab, click on the WebsiteURL Key in the value column.  

 ![image](images/20.jpeg) 

4.	This is a test webpage of Any Business, select the test chat widget on the bottom right to start a chat. 

 ![image](images/21.jpeg) 

5.	Customers can submit questions for self-service support. The FAQBucket includes a Word document containing frequently asked questions, which will be used as a reference for providing answers. For instructions on how to upload your own FAQ document, please see the next section, “Change FAQ document.”
    Example questions
    -	What is your return policy?
    -	How do I return an item?
    -	How can I contact support?
    -	Do you have a loyalty program?

 ![image](images/22.jpeg) 

_Note: Amazon Q is a generative AI-powered assistant that enables users to ask questions in natural language, without needing to match the exact wording found in company documents. If a user's question is related to information available in connected data sources, Amazon Q will understand the intent, identify relevant content, and provide an appropriate answer-even if the question is phrased differently than in the original document. For instance, if a document contains information about "What is your return and exchange policy?" and a customer asks, "I got my package and I want to return it," Amazon Q will recognize the connection and deliver the relevant answer. If the question is unrelated to any available information, Amazon Q will simply respond that it does not have an answer._

6.	At any stage the agent can say “speak to an agent” to be transferred to an agent via chat.
7.	Log the agent into Amazon Connect and set status to ready to accept the chat.

 ![image](images/23.jpeg) 

8.	Customers can move to voice > video and screenshare by select start call and enabling their camera.

 ![image](images/24.jpeg) 

9. Agents will receive a post-call summary following each interaction to automate their after-call work.

 ![image](images/30.jpeg) 

### How to update the FAQ document with your own data
1.	Login to your AWS account were you deployed the CloudFormation template.
2.	Navigate to CloudFormation.
3.	Select the stack name > Outputs and copy the FAQBucketName

 ![image](images/25.jpeg) 

4.	Navigate to S3 and search for the bucket name.

 ![image](images/26.jpeg) 

5.	The bucket will contain a single file. Please delete this file and upload your own document containing FAQ questions and answers.
    Note: Your document must meet the following requirements:
    - Accepted formats: plain text (.txt), Word document (.docx), or PDF (.pdf)
    - File size must be less than 1 MB
    - Only include text-remove any images, as Generative AI only processes text

## Summary 

This guide provides step-by-step instructions to deploy an Amazon Connect self-service customer experience solution.   Upon completion you will have a GenAI chat bot with web calling capability, and an OMNI Channel contact centre.

By following this implementation, you will have:
1. Amazon Connect platform
2. Self-service chatbot
3. Omnichannel interaction management (Chat, Voice, Video, Screen Sharing)
4. Agent assistant (Next Best Action)
5. Speech analytics capabilities
6. Automated post call summary

## Notice
Customers are responsible for making their own independent assessment of the information in this Guidance. This Guidance: (a) is for informational purposes only, (b) represents AWS current product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS products or services are provided “as is” without warranties, representations, or conditions of any kind, whether express or implied. AWS responsibilities and liabilities to its customers are controlled by AWS agreements, and this Guidance is not part of, nor does it modify, any agreement between AWS and its customers.

