# Genie context for transcript-driven graphics

Researched 2026-10-22. These are current official pages, not an archived verification of every statement at the video's publication date. The preceding practice was based on the uploaded narration and visual inspection, without this independent product research.

## Product model

- **Genie One:** a governed business-user entry point for questions, answers, dashboards, agents and apps. Chat searches for relevant Genie Agents first, then relevant assets if no matching agent is found. It can connect external sources. Source: https://docs.databricks.com/aws/en/genie-one/chat and https://www.databricks.com/product/genie/one
- **Genie Code:** technical data work inside the Databricks workspace, including notebooks, SQL, pipelines, analysis and dashboards. Source: https://www.databricks.com/product/genie/code
- **Genie Agents:** curated domain-specific interfaces with datasets, example SQL, expressions and instructions. Formerly called Genie Spaces. They can return queries, tables and visualizations; they are more specific than a generic autonomous-agent icon. Source: https://docs.databricks.com/aws/en/genie-agents/
- **Genie Ontology:** shared business context searched by Genie One and Genie Code. It combines modeled Unity Catalog semantics (metric views, domains, Pages) and inferred snippets from existing assets and usage. Examples include metric definitions, business rules and authoritative-source guidance. Snippets have authority scores and are gated by Unity Catalog permissions. Current documentation labels it Public Preview. Source: https://docs.databricks.com/aws/en/genie/genie-ontology

## Consequences for explanatory graphics

1. Definition: show a business user asking a concrete business question in One. Preserve a stable product referent.
2. Answer to action: preserve the same question, returned evidence and next action. A generic question/answer box removes the mechanism and practical meaning demonstrated by the source.
3. Product family: the video's cards introduce product roles. Their stacked arrangement is an editorial metaphor, not evidence of software dependency or execution order. Show architecture separately when explaining routing or shared context.
4. Ontology: show an ambiguous term such as active customer, then its governed definition, an authoritative source and the context being retrieved for an answer. Two input categories converge: explicitly modeled semantics and automatically inferred context. Avoid implying every snippet is manually curated or that every inference is certified truth.
5. Governance: show permissions applying to source assets and retrieval. A shield alone is a shorthand, not an explanation of permission gating.
6. Continuity: the next graphic state must answer the next explanatory question. Retain known entities and reveal only the new distinction.

## Available official visual references

Discovered in the official Genie One product page; not yet downloaded, visually reviewed or incorporated into a render:

- Official Genie SVG: https://www.databricks.com/sites/default/files/2026-05/icon-genie.svg
- Product screenshot: https://www.databricks.com/sites/default/files/2026-06/genie-product-page-business-teams-feature-1-new.png
- Product animation: https://www.databricks.com/sites/default/files/2026-06/genie-product-page-business-teams-feature-5.gif
- Documentation chat animation: https://assets.docs.databricks.com/_static/images/db1-chat.gif

## Fabric adaptation constraint

Do not simply replace Genie names with Fabric names. Verify Fabric's entity, relationship, grounding, action and governance mechanisms against its own documentation, then reuse the teaching structure where it fits. This research establishes Databricks context; it does not establish product equivalence with Fabric ontology.

## Production rule

Before generating a scene, record: spoken claim → intended understanding → verified product mechanism → graphic type → retained objects → state change and timing → supporting source. If the source graphic is a metaphor, label that in the production plan. Do not change a reference reconstruction into an architectural claim by accident.
