With the help of ChatGPT, I created a learning checklist for this challenge:

# 🧠 Visitor Counter Project Study Checklist (with Custom Domain via Azure Front Door)

A complete roadmap to learn everything you need to **build, deploy, and manage** a full serverless Visitor Counter web app hosted on Azure — using **HTML, CSS, JavaScript, Python, Git, GitHub, and Azure CLI** — with a **custom domain and HTTPS** via **Azure Front Door**.

---

## 🧩 1. HTML — Structure of the Webpage
**🎯 Goal:** Build a simple static page with linked JavaScript and styled layout.

- [ ] Understand basic HTML structure (`<!DOCTYPE html>`, `<head>`, `<body>`)
- [ ] Use semantic tags (`<h1>`, `<p>`, `<div>`) for content
- [ ] Add external JavaScript and CSS files (`<script src="">`, `<link rel="">`)
- [ ] Work with IDs and classes for element targeting
- [ ] Verify your page loads correctly in a browser

✅ **Milestone:** Create an `index.html` with a visible `<div id="visitors">` element.

---

## 🎨 2. CSS — Styling and Layout
**🎯 Goal:** Make your visitor counter page look clean and centered.

- [ ] Use inline, internal, and external CSS
- [ ] Style text (`font-family`, `color`, `font-size`)
- [ ] Learn box model basics (`margin`, `padding`, `border`)
- [ ] Use Flexbox or Grid for centering elements
- [ ] Apply background colors or simple themes

✅ **Milestone:** Page text is centered and visually balanced.

---

## ⚡ 3. JavaScript — Frontend Logic
**🎯 Goal:** Dynamically fetch and display the visitor count.

- [ ] Learn how to access DOM elements (`document.getElementById`)
- [ ] Add event listeners (`DOMContentLoaded`)
- [ ] Fetch data from an API (`fetch()`, `async/await`)
- [ ] Handle responses and errors gracefully (`try/catch`)
- [ ] Parse JSON (`response.json()`)
- [ ] Display API data dynamically in HTML

✅ **Milestone:** Page automatically fetches and displays a number from your Function endpoint.

---

## 🐍 4. Python — Backend Function Logic
**🎯 Goal:** Build a Python Azure Function that updates the counter in Cosmos DB.

- [ ] Understand Python functions, imports, and modules
- [ ] Learn how to handle exceptions (`try/except`)
- [ ] Create and activate virtual environments (`python3 -m venv .venv`)
- [ ] Install dependencies with `pip`
- [ ] Learn Azure SDK for Python (`azure.data.tables`, `azure.identity`)
- [ ] Return JSON responses using `json.dumps()`

✅ **Milestone:** Azure Function runs locally (`func start`) and returns a JSON response with a count.

---

## 🌐 5. Git & GitHub — Version Control and Automation
**🎯 Goal:** Manage project versions and automate deployment.

- [ ] Initialize a Git repository (`git init`)
- [ ] Stage and commit changes (`git add .`, `git commit -m ""`)
- [ ] Create and switch branches (`git branch`, `git checkout`)
- [ ] Push to GitHub (`git push origin main`)
- [ ] Add `.gitignore` for Python and VSCode files
- [ ] Create GitHub Secrets for Azure credentials
- [ ] Set up GitHub Actions workflows for CI/CD
- [ ] Debug failed workflows via GitHub Actions logs

✅ **Milestone:** Code pushes to GitHub automatically trigger deployment to Azure.

---

## ☁️ 6. Azure CLI — Cloud Resource Management
**🎯 Goal:** Deploy and manage all resources from the terminal.

- [ ] Log in and set your subscription (`az login`, `az account set`)
- [ ] Create and manage resource groups (`az group create`, `az group delete`)
- [ ] Create storage accounts (`az storage account create`)
- [ ] Upload static sites (`az storage blob upload-batch`)
- [ ] Create and configure Function Apps (`az functionapp create`, `az functionapp config`)
- [ ] Create Cosmos DB Table API resources (`az cosmosdb create`, `az cosmosdb table create`)
- [ ] Assign managed identities and roles (`az functionapp identity assign`, `az role assignment create`)
- [ ] Configure CORS for the Function App (`az functionapp cors add`)

✅ **Milestone:** You can deploy all cloud resources from your Debian terminal without using the Azure Portal.

---

## ☁️ 7. Azure Concepts — Understanding the Ecosystem
**🎯 Goal:** Know how each Azure service connects in your project.

- [ ] Understand what a **Resource Group** is (container for related resources)
- [ ] Understand what a **Storage Account** is (hosts the static site)
- [ ] Understand what a **Function App** is (runs backend Python logic)
- [ ] Understand what **Cosmos DB (Table API)** is (stores visit counts)
- [ ] Understand what **Managed Identity** is (secure passwordless service auth)
- [ ] Understand what **CORS** is (browser request security)
- [ ] Understand what **Azure Front Door** is (global load balancer + CDN + custom domain)
- [ ] Understand how **custom domains and HTTPS** work (SSL certificates automatically managed)

✅ **Milestone:** You can explain the full data flow:  
**Visitor → Custom Domain → Front Door → Static Website → Azure Function → Cosmos DB → Back to Browser**

---

## 🌍 8. Azure Front Door — Custom Domain + HTTPS Configuration
**🎯 Goal:** Serve your static site securely on your own domain.

- [ ] Purchase or manage your domain (from Namecheap, GoDaddy, etc.)
- [ ] Create an **Azure Front Door** instance (`az network front-door create`)
- [ ] Add your **static website endpoint** as the backend origin (from Blob Storage)
- [ ] Create a **frontend endpoint** in Front Door that matches your custom domain (e.g., `www.example.com`)
- [ ] Configure DNS with a **CNAME record** pointing to the Front Door endpoint
- [ ] Verify domain ownership in Azure
- [ ] Enable **HTTPS** (Azure-managed certificate)
- [ ] Test the public URL for HTTPS access
- [ ] Update your JavaScript `fetch()` calls to use your new domain (e.g., `https://www.example.com/api/VisitCounter`)

✅ **Milestone:** Your visitor counter site is available at your own domain, over HTTPS, served globally with Azure Front Door.

---

## ⚙️ 9. DevOps Concepts — Automation & Secrets
**🎯 Goal:** Secure and streamline deployments.

- [ ] Understand environment variables and secrets
- [ ] Know what CI/CD means and how it works
- [ ] Learn how GitHub Actions automates build + deploy steps
- [ ] Use GitHub Secrets for sensitive data (Azure credentials, keys)
- [ ] Learn to read GitHub Actions logs for debugging

✅ **Milestone:** Every code update is automatically built, tested, and deployed securely.

---

# 🎯 Final Mastery Check

| ✅ | Question | Can You Do It? |
|----|-----------|----------------|
| ☐ | Create and style a static HTML/CSS webpage |
| ☐ | Use JavaScript Fetch to call your Function App automatically |
| ☐ | Build and run a Python Azure Function locally and in Azure |
| ☐ | Push updates to GitHub and trigger CI/CD deployments |
| ☐ | Use Azure CLI to manage and deploy all resources |
| ☐ | Configure Azure Front Door with your custom domain |
| ☐ | Verify your website runs securely over HTTPS |
| ☐ | Explain how all Azure services work together in your system |

---

**💡 Local Testing Tip:**  
Before deploying to Azure, test your project locally:
```bash
# Start your Azure Function locally
func start

# Serve your static site locally
python3 -m http.server
