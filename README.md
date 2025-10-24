# The Cloud Resume Challenge, or How I Stumbled Through Azure for a Month
A great deal of digital ink has been spilled already about the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/) (hereafter "The Challenge"). This writeup will serve as a bit of a journal for my adventure!

## A little about me
I come from a *recreationally technical* background - I've dabbled in Linux since being a teenager, have always found working in the command line "neat", and I've always been the family go-to for tech-related questions. In my recent professional roles (in tech sales), I have come progressively closer and closer to the development side of things and, most recently, the wonderful world of RFPs, risk assessments, controls, etc. I've slowly had to become more conversant in cloud-related parlance, so, I thought, why not try jumping in to see how much I can learn. 

I hope my story, whatever comes of it, can serve as a source of learning (or cautionary tale?) for anyone trying to move into a more "technical" space - whether for a hobby or professionally.

Here goes!

## Step 1: AZ-900 Certification
This step was pretty straightforward. I am lucky to have access to some great digital resources through my library, specifically O'Reilly Learning, which granted me access to Jim Cheshire's course on the certification. 

In preparation for the exam, I did a great deal of practice tests on the Microsoft website. I booked my exam when I was consistentlt getting 90%+ on the practice tests. When I sat the exam, I was surprised to see that the format of many of the questions were quite different from the practice tests, and some of the content threw me for a bit of a curveball, but I still passed with an 857. If I can do it, you certainly can too.

## Step 2: HTML
Ok, so, I kind of cheated here and in **Step 3**. I have brushed up against HTML and CSS before in a previous role and also when putting together the website for my wife's business, but ChatGPT did play a big role here for this project - not only as a time saver but also as a learning tool.

>[!TIP] 
>If you are not a front-end developer (I am not), I enthusiastically recommend using generative AI to help with this part of the challenge. I had a clean HTML and CSS resume template in seconds, but the exercise of revising/customizing it served as a great learning experience.

## Step 3: CSS
Pretty much the same as Step 2.

## Step 4: Static Website
Setting up the static website was dead simple. Just uploaded my index.html and style.css to the blob. 

>[!TIP]
>Make sure the title of your html file matches the value you put in the **Static Website** blade of the blob resource. Took me a couple tries to get that right...

## Step 5: HTTPS
This is where things started to get dicey for me. I discovered that the Azure free trial I was on did not support the use of **Azure Front Door**, which is necessary for configuring HTTPS, so I went on a tangent learning expereince spelunking the subscription options. *However* I later remembered that Azure gave a $200 credit for the first 30 days of my new account, so I used the credits to activate Front Door. It seems this option is not particularly sustainable in the long term (~$50 CDN/month!), so I decided to work within the 30 day time frame and shut down the project upon completion, lest I incur unneccesary costs. 

## Step 6: DNS
It took me a surprisingly long time to troubleshoot this step. At first I thought it would be sufficient to use the Endpoint hostname from the Static Website, but I later discovered that using the Endpoint hostname of the Azure Front Door resource is actually the way to do it (in retrospect, seems pretty obvious). I use Porkbun, and it was pretty easy to configure once I knew which CNAME I had to use.

>[!TIP]
>The Endpoint hostname of your Azure Front Door resource is the answer/value for the CNAME that you should direct your custom domain! Remember the TXT secret as well!

## Step 7: Javascript
I got support form ChatGPT again for this step. I haven't really worked with Javascript before, so was unclear about how all the parts would fit together, so I asked ChatGPT for a step-by-step of how to set up the script for the counter on my website.

## Step 8: Database
I ran into an error when setting up the Cosmos DB Table API, it seems the default location was not eligble for deployment. I had to go back through the wizard an select a different location, then it worked as expected.

Afterward, I created the table using the parameters below:
| PartitionKey | RowKey   | Count           |
| ------------ | -------- | --------------- |
| counter      | visitors | (integer count) |


## Step 9: API
Setting up the Functions App was straightforward. I chose the lowest option for consumption and set the code to "python".

## Step 10: Python

## Step 11: Tests

## Step 12: Infrastructure as a Code

## Step 13: Source Control

## Step 14: CI/CD (Back end)

## Step 15: CI/CD (Front end)

## Step 16: Blog Post

## Thoughts and Next Steps
All this is well and dandy, but I'm not sure I like being held down to one cloud provider. So, for my next project, I'd like to transfer the project above into Terraform and try to deploy it into another provider, probably AWS.

