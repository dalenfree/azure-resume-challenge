# The Cloud Resume Challenge: My One-Month Journey Through Azure

[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Bicep](https://img.shields.io/badge/Bicep-0052CC?style=for-the-badge&logo=microsoft&logoColor=white)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/)

Much has been written about the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/). This writeup serves as a journal of my one-month journey exploring Azure. My goal was to transition from tech sales into a more technical, cloud-focused role, and this project provided immersive, hands-on experience.

---

## Skills Highlight

**Cloud & Infrastructure:** Azure (Blob Storage, Front Door, Function Apps, Cosmos DB, DNS, SSL/TLS), Azure CLI, Infrastructure as Code (ARM Templates, Bicep)  
**Programming & Scripting:** Python, JavaScript, HTML, CSS  
**DevOps & CI/CD:** GitHub Actions, YAML workflows, automated deployments, source control  
**Tools & IDEs:** VSCode, Git, ChatGPT, Porkbun domain management  
**Testing & Automation:** Python unit testing, mocking, patching  

---

## About Me

I come from a *recreationally technical* background — dabbling in Linux since my teens, enjoying command-line work, and often being the family tech support. In tech sales, I gradually moved closer to the development side, including RFPs, risk assessments, and controls.  

This project gave me a chance to dive into cloud concepts and hands-on development. My hope is that my experience can serve as guidance (or a cautionary tale) for anyone interested in getting "into the weeds" with cloud infrastructure.

---

## Step-by-Step Summary

| Step | Description | Tools/Skills Learned | Notes & Side Quests |
|------|------------|--------------------|-------------------|
| **1. AZ-900 Certification** | Completed Microsoft AZ-900 exam to build foundational cloud knowledge. | Azure fundamentals, Microsoft learning resources, practice tests | > [!TIP] Use practice tests extensively before booking the exam. Surprises may appear on the actual test format, though. |
| **2. HTML** | Brushed up on HTML with AI assistance. | HTML, ChatGPT | > [!TIP] AI like ChatGPT can save time and help you learn HTML structure efficiently, especially if you don't have much experience with web development. |
| **3. CSS** | Styled static website. | CSS, responsive design, ChatGPT | Same as Step 2. Templates and AI help a lot. |
| **4. Static Website** | Deployed `index.html` and `style.css` to Azure Blob Storage. | Azure Storage, static websites, deployment process | > [!TIP] Ensure the HTML file name matches the Static Website configuration in Azure Blob. |
| **5. HTTPS** | Configured custom domain using Azure Front Door. | Azure Front Door, SSL/TLS, domain mapping | > [!NOTE] Azure free trial may not allow Front Door. Use a $200 credit account for short-term testing. |
| **6. DNS** | Set up DNS records for custom domain (Porkbun). | CNAME, TXT records, DNS troubleshooting | > [!TIP] Point the CNAME to your Front Door endpoint, not the Blob Storage directly. Remember the TXT secret for verification. |
| **7. JavaScript** | Implemented visitor counter and front-end logic. | JavaScript, DOM manipulation (`DOMContentLoaded`), API integration, ChatGPT guidance | > [!TIP] Understanding DOM events like `DOMContentLoaded` is crucial for triggering frontend logic. |
| **8. Database** | Created Cosmos DB NoSQL database. | Cosmos DB, partition keys, JSON formatting, CORS troubleshooting | > [!NOTE] Table API may be restrictive; switching to NoSQL improved flexibility. |
| **9. API** | Set up Azure Function App to interact with database. | Azure Functions, Python runtime, HTTP GET/POST, VSCode, Git integration | > [!TIP] Use VSCode with Git to manage Azure Function code. Direct deployment via VSCode may be slow on Linux. |
| **10. Python** | Implemented backend logic for visitor count increments and retrieval. | Python, Cosmos DB SDK, error handling, API integration | > [!NOTE] Frontend JavaScript interacts via HTTP GET/POST. Debugging may require CLI deployment. |
| **11. Tests** | Wrote unit tests for the Function App. | Python testing, mocking, patching, ChatGPT guidance | > [!TIP] Learn `mock` and `patch` for testing API calls and DB interactions. |
| **12. Infrastructure as Code** | Automated deployments using ARM Templates and Bicep. | ARM Templates, Bicep, VSCode IaC plugin | > [!NOTE] Initial ARM Templates were replaced by Bicep for simplicity. Terraform can be explored later. |
| **13. Source Control** | Managed project using Git and GitHub. | Git, GitHub, VSCode integration | > [!TIP] Commit frequently; use VSCode Git integration for smooth workflow. |
| **14. CI/CD (Backend)** | Automated deployment of Function App. | GitHub Actions, YAML workflows, Azure CLI, Entra ID federated credentials | > [!TIP] Use Entra ID federated credentials for secure automated login. Specify `on -> push -> paths` to avoid unnecessary deployments. |
| **15. CI/CD (Frontend)** | Automated deployment of static website to Blob Storage. | GitHub Actions, Blob Storage, workflow variables, CLI commands (`--nowait`) | > [!TIP] Keep a running list of resource names and endpoints. Add `--nowait` to avoid hanging purge commands. |
| **16. Blog Post** | Documented learnings for personal and professional sharing. | Technical writing, cloud documentation, blog platforms | > [!TIP] Sharing your process helps others and solidifies your own understanding. |

---

## Key Tips & Learnings

- **AI Assistance:** ChatGPT was invaluable for learning and coding guidance.  
- **CLI Efficiency:** Azure CLI is faster and more reliable than the GUI for complex deployments.  
- **IaC Value:** Using Bicep/ARM Templates improves repeatability and reduces manual errors.  
- **Documentation & Organization:** Maintain a list of endpoints, variables, and resource names to save hours.  
- **Continuous Learning:** Integrating frontend, backend, and cloud services requires patience and incremental learning.

---

## Reflection

This project allowed me to:  

- Gain hands-on experience with Azure, Cosmos DB, and Function Apps  
- Develop skills in Python, JavaScript, HTML/CSS, and CI/CD  
- Deepen my knowledge of the technical aspects of the cloud, assisting me in my current role and positioning me for a career trajectory with a more cloud-oriented, technical focus   

The Cloud Resume Challenge was a meaningful first step .

---

## Next Steps

- Continue to deepen knowledge of Azure services (e.g., App Services, Kubernetes)  
- Explore Terraform and multi-cloud IaC
- Continue building integrated projects combining backend, frontend, and cloud skills
