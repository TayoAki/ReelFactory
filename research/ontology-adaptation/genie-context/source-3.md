Source: https://docs.databricks.com/aws/en/genie-one/chat
Retrieved: 2026-10-22

[Skip to main content](https://docs.databricks.com/aws/en/genie-one/chat#__docusaurus_skipToContent_fallback)

On this page

Last updated on **Oct 16, 2026**

Chat in Genie One is a unified, full-screen natural-language interface for business users to ask data questions. It first searches available Genie Agents for a match, then searches across dashboards, queries, and metric views. You can also connect external sources (such as Google Drive and SharePoint) so chat can answer from your company documents and schedule recurring chat tasks that post results back as a thread.

![Chat in Genie.](https://assets.docs.databricks.com/_static/images/db1-chat.gif)

## How chat works [​](https://docs.databricks.com/aws/en/genie-one/chat\#how-chat-works "Direct link to How chat works")

When you submit a question to chat:

1. It searches available Genie Agents for one relevant to your question.
2. If a matching Genie Agent is found, it uses that space to generate a response.
3. If no matching Genie Agent is found, it searches for relevant data assets to answer your question.

To give chat access to your company documents, connect external data sources such as Google Drive, SharePoint, GitHub, Glean, and Atlassian. See [Connect Genie One to external tools and sources](https://docs.databricks.com/aws/en/genie-one/external-sources).

To open chat, click **New chat** from the sidebar or use **Ask** mode in the search bar. You must have the CAN USE permission on at least one SQL warehouse to use chat.

### Select compute [​](https://docs.databricks.com/aws/en/genie-one/chat\#select-compute "Direct link to Select compute")

Chat uses **Auto** compute by default, which automatically selects the best available SQL warehouse and is recommended for most users. To use a specific warehouse instead:

1. Click **•••** in the top right.
2. Click **Manage compute**.
3. Select your SQL warehouse.

## Manage chats in the sidebar [​](https://docs.databricks.com/aws/en/genie-one/chat\#manage-chats-in-the-sidebar "Direct link to manage-chats-in-the-sidebar")

Your recent chats appear in the sidebar. Hover over a chat and click the ![Kebab menu icon.](<Base64-Image-Removed>) kebab menu to manage it:

- **Pin a chat**: Select **Pin** to keep the chat at the top of the sidebar for quick access. Pinned chats stay at the top until you unpin them.
- **Rename a chat**: Select **Rename**, enter a new name, and confirm to give the chat a clearer title.

## Create a Genie Agent from a conversation [​](https://docs.databricks.com/aws/en/genie-one/chat\#create-a-genie-agent-from-a-conversation "Direct link to create-a-genie-agent-from-a-conversation")

You can turn the context from a chat conversation into a reusable Genie Agent. This is helpful when a conversation builds up context that you want to save and apply to future questions, such as a sales KPI analysis, business report formatting guidance, or other domain-specific instructions.

note

To create a Genie Agent from Genie One, you must have the **Workspace access** or **Databricks SQL access** entitlement. Users with only **Consumer access** and account users without workspace membership can't create Genie Agents from Genie One. See [Manage entitlements](https://docs.databricks.com/aws/en/security/auth/entitlements).

### Create an agent [​](https://docs.databricks.com/aws/en/genie-one/chat\#create-an-agent "Direct link to create-an-agent")

You can create a Genie Agent from a conversation in two ways:

- Ask Genie One to save the conversation's context as an agent.
- Click the overflow menu ( **•••**) under an answer, then click **Create Agent**.

![The overflow menu under a Genie One answer, showing the Create Agent option.](https://docs.databricks.com/aws/en/assets/images/create-agent-from-chat-813aa0d9dd8de43ca88c9964a3580342.png)

To create an agent in a conversation, tell Genie One what you want the agent to capture:

prompt

```text
Save this sales KPI analysis as an agent so I can reuse it.
```

After Genie One creates the agent, you can open it in your workspace to fine-tune its context, instructions, and data assets. To learn more about Genie Agents, see [Genie Agents](https://docs.databricks.com/aws/en/genie-agents/).

### Edit an agent [​](https://docs.databricks.com/aws/en/genie-one/chat\#edit-an-agent "Direct link to Edit an agent")

You can ask Genie One to change an agent's context in a conversation. For example, you can add tables or change an agent's instructions in natural language.

prompt

```text
Add the sales.forecast table to my sales KPI agent.
```

![Genie One updating a Genie Agent&#39;s context in a conversation, showing the changes it made.](https://docs.databricks.com/aws/en/assets/images/edit-agent-context-affe47f12899b33ab83e97eb50f6dc02.png)

### Delete an agent [​](https://docs.databricks.com/aws/en/genie-one/chat\#delete-an-agent "Direct link to Delete an agent")

You can ask Genie One to delete an agent in a conversation. Genie One asks you to confirm before it deletes the agent.

prompt

```text
Delete my sales KPI agent.
```

![The confirmation prompt that Genie One shows before it deletes a Genie Agent.](https://docs.databricks.com/aws/en/assets/images/delete-agent-043d2e1bb5993e63d851aeacd3ecb24b.png)

## Genie Ontology [​](https://docs.databricks.com/aws/en/genie-one/chat\#genie-ontology "Direct link to genie-ontology")

Genie One uses Genie Ontology, the unified context layer that gives Genie a business-aware map of your organization. It combines modeled context you govern in Unity Catalog semantics, such as metric views, domains, and Pages, with context Genie infers automatically from your assets and usage. Genie One and Genie Code search the same ontology, so context you curate once applies to both surfaces.

To see which knowledge sources Genie One used to answer your question, click the ![Snippet icon.](<Base64-Image-Removed>) citation icons in a response.

For a full description of Genie Ontology, including inferred context, authority scoring, and permission gating, see [Genie Ontology](https://docs.databricks.com/aws/en/genie/genie-ontology).

## Add workspace instructions for chat [​](https://docs.databricks.com/aws/en/genie-one/chat\#add-workspace-instructions-for-chat "Direct link to add-workspace-instructions-for-chat")

Workspace admins can add custom instructions that apply to every chat conversation in the workspace. Instructions can include information about your organization's data conventions, preferred terminology, or guidelines for how chat should respond.

To add workspace instructions, create a Markdown file at the following path in your workspace:

```text
/Workspace/.genie_workspace_instructions.md
```

Instructions must be under 20,000 characters. Chat reads this file automatically with no additional configuration required. Instructions apply to chat only and do not affect Genie Agents or Genie Code.

For best practices on adding custom instructions, see [Best practices for Genie Code instructions](https://docs.databricks.com/aws/en/genie-code/instructions#limits).

## Skills [​](https://docs.databricks.com/aws/en/genie-one/chat\#skills "Direct link to skills")

Skills let you extend chat in Genie One with custom capabilities tailored to your needs. By default, a skill is available only to you, but you can share it with your team. See [Share a skill with your team](https://docs.databricks.com/aws/en/genie-one/chat#share-skills). Skills are loaded automatically when Genie One determines they are relevant to your request, and you can invoke a skill manually by typing `/` followed by its name.

A skill can include multiple files and sub-folders, up to three folders deep and 50 files or folders per skill. Skills can contain text files only. Images, PDFs, and other binary files are not supported.

note

For agent skills in Genie Code, see [Extend Genie Code with agent skills](https://docs.databricks.com/aws/en/genie-code/skills).

### Create a skill [​](https://docs.databricks.com/aws/en/genie-one/chat\#create-a-skill "Direct link to Create a skill")

prompt

Tell Genie One to do this for you:

```text
Create a skill that summarizes weekly sales trends for my region.
```

Genie One creates the skill and saves it to your workspace at `/Workspace/Users/{email}/.assistant/skills/`.

### Edit a skill [​](https://docs.databricks.com/aws/en/genie-one/chat\#edit-a-skill "Direct link to Edit a skill")

To edit a skill, ask Genie One to make changes in a conversation, then review the changes in the sidebar. You can also manage a skill from its page:

1. In the left navigation, click **Customizations**, then click **Skills**.
2. Select the skill.
3. From the drop-down menu next to **Share** in the top right, select **Edit with Genie** to change the skill in a conversation, or **Open in workspace editor** to edit its files directly.

To delete a skill, follow the same steps and select **Remove skill** from the drop-down menu.

### Invoke a skill [​](https://docs.databricks.com/aws/en/genie-one/chat\#invoke-a-skill "Direct link to Invoke a skill")

Genie One automatically loads skills when they are relevant to your request. To invoke a skill, type `/` followed by its name in the chat input.

### Share a skill with your team [​](https://docs.databricks.com/aws/en/genie-one/chat\#share-a-skill-with-your-team "Direct link to share-a-skill-with-your-team")

Beta

This feature is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types) and requires two previews:

- An account admin must turn on the **Enhanced Unity AI Gateway** preview from the account console [Previews page](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews#account).
- A workspace admin must turn on the **Unity Gateway skills in Genie** preview from the workspace [Previews page](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews#workspace).

You can publish a skill and share it with teammates. Skills are governed by Unity Gateway, so the same catalog and schema privileges that protect your other data control who can publish and use them:

- To publish a skill, you need `USE CATALOG`, `USE SCHEMA`, and `CREATE VOLUME` on the target schema.
- To install and use a shared skill, you need `USE CATALOG`, `USE SCHEMA`, and `READ VOLUME` on the schema that holds it.

For the full privilege model, including the privileges needed to update a published skill, see [Grant access to skills](https://docs.databricks.com/aws/en/ai-gateway/govern-skills#grant-access).

To publish a skill and share it:

1. In the left navigation, click **Customizations**, then click **Skills**.
2. Select the skill, then click **Share**.
3. Under **Publish to**, select a catalog and schema.
4. Add the users, groups, or service principals to share with, and set the general access level.
5. Click **Done**.

### Find and install shared skills [​](https://docs.databricks.com/aws/en/genie-one/chat\#find-and-install-shared-skills "Direct link to Find and install shared skills")

On the customization page, skills that teammates shared with you appear next to your skills. Install a skill to use it in your chats, and uninstall it to stop using it.

You can also browse skills from chat: click **+** in the message composer, then select **Skills** \> **Browse skills**.

### Use shared skills in scheduled tasks [​](https://docs.databricks.com/aws/en/genie-one/chat\#use-shared-skills-in-scheduled-tasks "Direct link to Use shared skills in scheduled tasks")

Skills you install are available in [scheduled tasks](https://docs.databricks.com/aws/en/genie-one/chat#scheduled-tasks), including tasks shared with your team, so recurring runs apply the same skills.

### Skill limitations [​](https://docs.databricks.com/aws/en/genie-one/chat\#skill-limitations "Direct link to Skill limitations")

Uploading files to a skill isn't supported in the Genie One UI. To add files, upload them from Catalog Explorer the same way you would for a volume: click ![Data icon.](<Base64-Image-Removed>)**Catalog**, browse to the skill in the catalog and schema you published it to, then upload your files. See [Use Catalog Explorer](https://docs.databricks.com/aws/en/volumes/volume-files#use-catalog-explorer).

## Scheduled tasks [​](https://docs.databricks.com/aws/en/genie-one/chat\#scheduled-tasks "Direct link to scheduled-tasks")

Scheduled tasks run automatically at a specified time and post the results in a chat thread. When a task runs, chat sends you an email with the results, including any visualizations, and a PDF attachment of the task's output.

You can create a scheduled task in two ways:

- Type a request in natural language in chat, for example: _"Send me a daily briefing of all new customer reviews for my store location."_ Chat might ask clarifying questions, such as the time or which location to use, then creates the task and adds it to the **Schedules** section.

- In the sidebar, click **Schedules**, then click the drop-down menu next to **\+ Create in chat** and select **Create manually**.

![Create scheduled task manually](https://docs.databricks.com/aws/en/assets/images/create-in-chat-f3e6afaa9b6a28aa35311cc62c1d7800.png)

Fill in the **Title**, **Instructions**, **Connections**, **Schedule**, and **Timezone**, then click **Create**.

![Create scheduled task dialog](https://docs.databricks.com/aws/en/assets/images/create-scheduled-task-1da7de96363e546de22dd03bfcac60f9.png)


To view past runs, edit, or delete a scheduled task, click the task in the **Scheduled tasks** section. Each run opens in a chat thread.

When you author a scheduled task, select **Run now** to run it immediately without waiting for the next scheduled time.

To reference a scheduled task in a new request, @mention it in chat.

## Recall past conversations [​](https://docs.databricks.com/aws/en/genie-one/chat\#recall-past-conversations "Direct link to recall-past-conversations")

Genie One remembers your past conversations and can draw on them to shape its answers, so you can build on earlier work without repeating yourself. Genie One only references your own conversations. This capability is always available and requires no setup.

Most of the time, Genie One draws on your conversation history automatically when earlier context is relevant, rather than only when you ask it to recall a past thread. When a previous conversation is used for context, it adds a citation that links back to the original conversation, just like any other source.

You can also draw on your past conversations yourself in two ways:

- **Bring past context into your current conversation.** Reference an earlier conversation to pull its context into the chat you're already in, without navigating away.
- **Find and reopen a past conversation.** Search by content to locate an earlier conversation, then reopen it to continue that thread.

For example, to drill down from a past conversation without leaving your current one:

prompt

```text
Remember when we talked about ARR last quarter? Let's drill down from that conversation and break it out by region.
```

## Personalized starter questions [​](https://docs.databricks.com/aws/en/genie-one/chat\#personalized-starter-questions "Direct link to personalized-starter-questions")

Beta

This feature is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). To use it, a workspace admin must turn on **Personalized Genie One Starter Questions** from the **Previews** page. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).

When personalized starter questions are enabled, the Genie One home page shows a small number of suggested questions tailored to you. Each one is a single-line prompt. Select a question to open a chat with it already entered, so you can start exploring your data.

### How questions are personalized [​](https://docs.databricks.com/aws/en/genie-one/chat\#how-questions-are-personalized "Direct link to How questions are personalized")

Genie One generates starter questions for you from your own recent Databricks activity: the tables, AI/BI dashboards, Genie Agents, and notebooks that you frequently use, recently viewed, or marked as favorites. If you have little recent activity, Genie One suggests questions based on assets that are popular across your workspace instead.

### Data access and privacy [​](https://docs.databricks.com/aws/en/genie-one/chat\#data-access-and-privacy "Direct link to Data access and privacy")

Starter questions only reference assets that you already have access to. They are generated using your own permissions, so they never surface data outside your access. Generation uses only asset metadata, such as names and types. It never reads the contents of your tables, dashboards, or notebooks.

### Availability [​](https://docs.databricks.com/aws/en/genie-one/chat\#availability "Direct link to Availability")

Personalized starter questions are in Beta. Workspace admins control access from the **Previews** page, as noted at the start of this section. When the feature is not enabled for a workspace, the home page shows a small set of generic default starter questions instead.

![The Genie One home page showing two personalized starter questions below the chat box.](https://docs.databricks.com/aws/en/assets/images/personalized-starter-questions-478a68e0861eecf3734e5296cb40052f.png)

### Limitations for personalized starter questions [​](https://docs.databricks.com/aws/en/genie-one/chat\#limitations-for-personalized-starter-questions "Direct link to Limitations for personalized starter questions")

Personalized starter questions are cached for each user and refresh periodically, so they might not reflect your most recent activity immediately.

For more about Genie One, see [Use Genie One](https://docs.databricks.com/aws/en/genie-one/).

## Add to Genie One's memory [​](https://docs.databricks.com/aws/en/genie-one/chat\#add-to-genie-ones-memory "Direct link to add-to-genie-ones-memory")

Genie One can retain specific facts you provide as memories and apply them in later conversations, so you don't need to repeat the same context every time you chat. Genie One's memories are private to you and aren't shared with other users.

Genie One saves a memory when you explicitly ask it to. To create a memory, tell Genie One what to remember in a conversation:

prompt

```text
Remember that I report all revenue in USD and my fiscal year starts in February.
```

Genie One automatically applies your saved memories to future conversations.

Genie One can also suggest a memory when it detects a fact worth remembering in your request that you did not explicitly ask it to save. It asks you to confirm before saving, and you can approve, modify, or reject the suggested memory.

When Genie One applies a memory, it includes a citation for the memory it used. You can give that memory a thumbs-up or thumbs-down to let Genie One know whether it's helpful. If a memory is wrong or out of date, ask Genie One to update or delete it directly in a conversation.

## Upload a file [​](https://docs.databricks.com/aws/en/genie-one/chat\#upload-a-file "Direct link to upload-a-file")

Upload CSV, Excel, PDF, image, Word, and PowerPoint files directly into a chat conversation to analyze them in natural language alongside your other data. Uploaded files are private to the conversation you add them to, and only you can access them.

To upload a file, select ![Plus icon.](<Base64-Image-Removed>) in the message composer, then **![Paperclip icon.](<Base64-Image-Removed>) Add files**. You can also drag and drop files onto the composer or paste them from your clipboard. To see the files in a conversation, select ![Plus icon.](<Base64-Image-Removed>) and open the **Uploaded files** list.

![Genie One composer with the add menu open, showing the Add files option](https://docs.databricks.com/aws/en/assets/images/upload-file-498a3c89cbaa10f06354cb3a2a20228e.png)

File requirements:

- Each CSV or Excel (`.xlsx` or `.xls`) file must be smaller than 200 MB. An Excel file can contain multiple sheets. To query a specific sheet, reference it by name.
- Each PDF must be smaller than 20 MB and contain no more than 100 pages. Genie One reads up to 4,000 characters per page.
- Each image (PNG, JPG, or JPEG) must be smaller than 5 MB. Genie One automatically downscales larger images.
- You can upload Word (`.docx`) and PowerPoint (`.ppt` or `.pptx`) files.
- You can upload up to 100 files per conversation, and up to 5 files in a single action.

Databricks stores uploaded files in a Unity Catalog managed volume, in customer-managed root storage on classic workspaces or in [default storage](https://docs.databricks.com/aws/en/storage/default-storage) on serverless workspaces. For details, see [Upload a file](https://docs.databricks.com/aws/en/genie-agents/file-upload#upload).

Uploaded files have no fixed retention period and no configurable lifecycle policy. They remain until you remove them or delete the conversation. For details, see [Remove a file](https://docs.databricks.com/aws/en/genie-agents/file-upload#remove).

## Search the web [​](https://docs.databricks.com/aws/en/genie-one/chat\#search-the-web "Direct link to search-the-web")

Beta

This feature is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). To use it, a workspace admin must turn on **Web search in Genie Code and Genie One** from the **Previews** page. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).

Genie One can search the public web to answer questions that need current information, such as recent release notes, third-party documentation, or news. Genie One decides when to search based on your request and cites the sources it uses. Each source appears in the response as a link you can open.

Web search has the following requirements:

- The workspace must have [partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered) enabled.
- The workspace must be in an eligible geo (Americas or Europe), or have [cross-geography processing enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing).
- For workspaces with the [compliance security profile](https://docs.databricks.com/aws/en/security/privacy/enhanced-security-compliance) enabled, web search is only supported for HIPAA. Other compliance standards are not supported.

## Code execution [​](https://docs.databricks.com/aws/en/genie-one/chat\#code-execution "Direct link to Code execution")

Preview

This feature is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types).

Genie One can run code in a secure, isolated sandbox to take on work that goes beyond SQL, such as advanced analyses and creating spreadsheets and presentations. Code runs on your behalf using only the permissions you already have. See [Code execution in Genie One](https://docs.databricks.com/aws/en/genie-one/code-execution).

## Documents [​](https://docs.databricks.com/aws/en/genie-one/chat\#documents "Direct link to Documents")

Ask Genie One to draft a shareable document from any chat conversation. The document opens in a canvas pane alongside the chat, where you can edit and share it. See [Documents in Genie One](https://docs.databricks.com/aws/en/genie-one/documents).

## Connect to external tools and sources [​](https://docs.databricks.com/aws/en/genie-one/chat\#connect-to-external-tools-and-sources "Direct link to Connect to external tools and sources")

Connect external data sources such as Google Drive, SharePoint, GitHub, Glean, and Atlassian to a chat conversation in Genie One. See [Connect Genie One to external tools and sources](https://docs.databricks.com/aws/en/genie-one/external-sources).

## Share a chat [​](https://docs.databricks.com/aws/en/genie-one/chat\#share-a-chat "Direct link to share-a-chat")

You can share a chat conversation with all users in your account as read-only.

1. Click **Share** in the upper-right corner of the conversation.

2. Select **Anyone in this account**.

3. Click **![Link icon.](<Base64-Image-Removed>) Copy link** and share the link with others.

![Share a chat conversation](https://docs.databricks.com/aws/en/assets/images/share-chat-edfd2ad6819af1a574eb04929b75c08a.png)


To make a conversation private again, click **Share** and select **Only me**.

## Limitations [​](https://docs.databricks.com/aws/en/genie-one/chat\#limitations "Direct link to Limitations")

- File upload is not currently supported for users who have only [consumer access](https://docs.databricks.com/aws/en/ai-bi/consumers/), or in the [Genie mobile app](https://docs.databricks.com/aws/en/genie-one/mobile).
- Workspaces with many Genie Agents might experience reduced routing accuracy.

## Additional resources [​](https://docs.databricks.com/aws/en/genie-one/chat\#-additional-resources "Direct link to -additional-resources")

- [Use Genie One](https://docs.databricks.com/aws/en/genie-one/)
- [Create a connection](https://docs.databricks.com/aws/en/query-federation/database-federation#connection)

On this page

- [How chat works](https://docs.databricks.com/aws/en/genie-one/chat#how-chat-works)
  - [Select compute](https://docs.databricks.com/aws/en/genie-one/chat#select-compute)
- [Manage chats in the sidebar](https://docs.databricks.com/aws/en/genie-one/chat#manage-chats-in-the-sidebar)
- [Create a Genie Agent from a conversation](https://docs.databricks.com/aws/en/genie-one/chat#create-a-genie-agent-from-a-conversation)
  - [Create an agent](https://docs.databricks.com/aws/en/genie-one/chat#create-an-agent)
  - [Edit an agent](https://docs.databricks.com/aws/en/genie-one/chat#edit-an-agent)
  - [Delete an agent](https://docs.databricks.com/aws/en/genie-one/chat#delete-an-agent)
- [Genie Ontology](https://docs.databricks.com/aws/en/genie-one/chat#genie-ontology)
- [Add workspace instructions for chat](https://docs.databricks.com/aws/en/genie-one/chat#add-workspace-instructions-for-chat)
- [Skills](https://docs.databricks.com/aws/en/genie-one/chat#skills)
  - [Create a skill](https://docs.databricks.com/aws/en/genie-one/chat#create-a-skill)
  - [Edit a skill](https://docs.databricks.com/aws/en/genie-one/chat#edit-a-skill)
  - [Invoke a skill](https://docs.databricks.com/aws/en/genie-one/chat#invoke-a-skill)
  - [Share a skill with your team](https://docs.databricks.com/aws/en/genie-one/chat#share-a-skill-with-your-team)
  - [Find and install shared skills](https://docs.databricks.com/aws/en/genie-one/chat#find-and-install-shared-skills)
  - [Use shared skills in scheduled tasks](https://docs.databricks.com/aws/en/genie-one/chat#use-shared-skills-in-scheduled-tasks)
  - [Skill limitations](https://docs.databricks.com/aws/en/genie-one/chat#skill-limitations)
- [Scheduled tasks](https://docs.databricks.com/aws/en/genie-one/chat#scheduled-tasks)
- [Recall past conversations](https://docs.databricks.com/aws/en/genie-one/chat#recall-past-conversations)
- [Personalized starter questions](https://docs.databricks.com/aws/en/genie-one/chat#personalized-starter-questions)
  - [How questions are personalized](https://docs.databricks.com/aws/en/genie-one/chat#how-questions-are-personalized)
  - [Data access and privacy](https://docs.databricks.com/aws/en/genie-one/chat#data-access-and-privacy)
  - [Availability](https://docs.databricks.com/aws/en/genie-one/chat#availability)
  - [Limitations for personalized starter questions](https://docs.databricks.com/aws/en/genie-one/chat#limitations-for-personalized-starter-questions)
- [Add to Genie One's memory](https://docs.databricks.com/aws/en/genie-one/chat#add-to-genie-ones-memory)
- [Upload a file](https://docs.databricks.com/aws/en/genie-one/chat#upload-a-file)
- [Search the web](https://docs.databricks.com/aws/en/genie-one/chat#search-the-web)
- [Code execution](https://docs.databricks.com/aws/en/genie-one/chat#code-execution)
- [Documents](https://docs.databricks.com/aws/en/genie-one/chat#documents)
- [Connect to external tools and sources](https://docs.databricks.com/aws/en/genie-one/chat#connect-to-external-tools-and-sources)
- [Share a chat](https://docs.databricks.com/aws/en/genie-one/chat#share-a-chat)
- [Limitations](https://docs.databricks.com/aws/en/genie-one/chat#limitations)
- [Additional resources](https://docs.databricks.com/aws/en/genie-one/chat#-additional-resources)

Was this page helpful?

YesNo

Send feedback

Ask Genie

Open Genie

|     |     |
| --- | --- |
|  |  |

