# python_automation_framework

## The main purpose:
This is a placeholder repo for an automation framework that I'm building in Python language. The idea is to write a great number of feature tests using Gherking language based on a sample app (described in a section below) and then use some of the most popular languages like Java, Python, Ruby and maybe even C# to create separate automation frameworks for the each feature tests. 
The very first framework will be written using Java, because it seems to be one of the most popular languages in automation testing. Once this one is completed I'll use the same list of feature tests (written in Gherking language) and I'll port the first framework to the other programming languages mentioned above. I've added different repositiories for each programming language where I'm planning to add the code.
I'll make sure of implementing the most popular best practices mentioned out there, like: Page Object Model, Page Factory and BDD. It's worth to mention that I'm not a guru in this field, so I'm working hard on complementing my actual knowledge by following experienced Automation Engineers like Angie Jones and many more.
Finally, once I start to upload my code and if you believe that there is something that can be improved please do not hesitate on conacting me to come up together with better solutions.

## What motivates me to do this?
I believe that a great way to learn is to see real life automation projects implemented and use them as a base or as inspiration to create your own testing frameworks. Something that made me think that this would be useful is that at lynda.com (the training site) they implemented a series of videos called "Code Clinic" where they find different solutions for the same list of problems using different programming languages, this has been well accepted by the crowd (including me!). So I though it would be a great idea to implement a similar approach with automation frameworks. 
This will be NOT the ultimate solution for anyone who wants to create an automation framework for its project, however this will be a great resource for those that are getting started in this field and are seeking for examples and/or inspiration.
At some point I'll also document how these frameworks work, so that people without experience can get rolling with it.

## The sample application:
I decided to spin up a free tier instance on AWS EC2 and then installed Wordpress in it. After that I added the WooCommerce plugin and loaded the store with some sample data. The purpose of this is to have a sample system that covers the 3 tier testing levels of an application:
- Tier 1: Rest API
    - WooCommerce comes with a Rest API that can be used to perform a great variety of actions
- Tier 2: UI/UI (including mobile testing)
    - WC comes with a minimalistic template, which also comes with responsive support for mobile users. This allows a good list of possible tests to be automated.
- Tier 3: Security / Performance
    - At some point I would also like to write some tests for performance and security testing.
    - Since this sample application is running on an AWS host, there is a wide list of possible testing scenarios to achieve this.

> If anyone feels interested about this project and wants to collaborate, just let me know. I would be excited to work as a team.
