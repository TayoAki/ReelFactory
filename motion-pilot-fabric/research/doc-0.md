Table of contents Exit editor mode

Ask LearnAsk Learn

Reading modeTable of contents[Read in English](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)Add to CollectionsAdd to Plans[Edit](https://github.com/MicrosoftDocs/fabric-docs/blob/main/docs/iq/ontology/overview.md)

* * *

Copy MarkdownPrint

* * *

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#) or changing directories.


Access to this page requires authorization. You can try changing directories.


# What is ontology (preview)?

Feedback

Summarize this article for me


The **ontology (preview)** item in Microsoft Fabric IQ provides a shared, machine-understandable representation of your business. It defines the concepts that matter to your organization, such as customers, products, assets, orders, and locations, along with their properties, how they relate, and the rules and metrics that give them business meaning. You then bind these definitions to enterprise data so people, applications, and AI agents can use the same vocabulary and context.

Important

This feature is in [preview](https://learn.microsoft.com/en-us/fabric/fundamentals/preview).

Important

For ontology known issues, see the [Microsoft Fabric known issues site](https://support.fabric.microsoft.com/known-issues/) and search for _ontology_. For troubleshooting details, see [Troubleshoot ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/resources-troubleshooting).

Important

The old experience of ontology retires on Jan 31, 2027. For more, see [Migrate from old experience](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#migrate-from-old-experience).

Ontology helps bridge the gap between how data is physically stored and how your business understands it. Instead of requiring every consumer to interpret tables, columns, measures, and joins independently, an ontology supplies reusable business concepts and source mappings across domains. This shared context can support analytics, real-time operational experiences, and AI agents that need consistent definitions and relationships.

[Section titled: Why use an ontology?](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#why-use-an-ontology)

## Why use an ontology?

Organizations often represent the same business concept differently across data sources, semantic models, applications, and teams. Ontology provides a common context layer that lets you:

- **Model the business in business terms.** Define entities, properties, relationships, rules, metrics, and hierarchies independently of any single physical table.
- **Build on existing semantic investments.** Optionally generate an ontology from Power BI semantic models to retain relevant tables, columns, relationships, calculated columns, and source-owned DAX measures.
- **Connect concepts to enterprise data.** Bind ontology definitions to supported Fabric data sources without requiring the ontology to become a separate data store.
- **Give AI agents shared context.** Ground agent experiences in governed definitions, relationships, metrics, rules, and source mappings instead of relying only on raw schemas or prompts.
- **Manage the model as it evolves.** Organize definitions with namespaces, reuse common concepts through inheritance, create named versions, and use Fabric permissions and lifecycle tooling.

[Section titled: How ontology fits in Fabric IQ](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#how-ontology-fits-in-fabric-iq)

## How ontology fits in Fabric IQ

Ontology is the **business context and semantic modeling layer** between enterprise data and the experiences that consume it. It stores and serves ontology definitions and bindings (it isn't itself a general-purpose data-query engine). Agent and visualization experiences use the ontology as context and execute against the appropriate bound data sources.

The following diagram illustrates that relationship.

[![Graphic showing how ontology in Fabric gives a live, unified view of the business.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview/ontology-fabric-iq-overview.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview/ontology-fabric-iq-overview.png#lightbox)

Ontology aligns with familiar semantic-model constructs while extending them with ontology-specific modeling concepts. You can represent tables, columns, measures, and relationships alongside entity hierarchies, business rules, source bindings, namespaces, and other semantic metadata. You can build an ontology from scratch, or you can generate it directly from semantic models. This option helps you extend existing semantic models into operational and agentic scenarios without having to rebuild their business meaning from scratch when you already have it defined.

[Section titled: Key capabilities](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#key-capabilities)

## Key capabilities

[Section titled: Unified semantic modeling](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#unified-semantic-modeling)

### Unified semantic modeling

Define reusable **entity types**, their **properties**, and the **relationships** between them. The updated ontology model supports more flexible representations, including keyless entity types, relationships without dedicated join tables, namespaces, entity hierarchies, and reuse through inheritance. These capabilities help you model business domains without requiring you to reshape the source data solely to fit the ontology.

For more information, see [Create entity types in ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-entity-types).

[Section titled: Alignment with Power BI semantic models](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#alignment-with-power-bi-semantic-models)

### Alignment with Power BI semantic models

One way to create an ontology is to generate it from a Power BI semantic model to reuse existing business definitions. Semantic-model tables and relationships provide the starting structure, while ontology adds business context and capabilities for operational and agent-based consumption. The updated experience expands semantic-model alignment to include calculated columns and DAX measures.

Measures from a source semantic model appear in ontology as **metrics** associated with the relevant entities. The source semantic model remains the owner of the DAX expression, while ontology retains the metric's source and business context so agents can recognize and use the organization's defined calculations rather than recreating them.

For more information, see [Generate an ontology (preview) from semantic models](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-generate-from-semantic-models).

[Section titled: Flexible data bindings](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#flexible-data-bindings)

### Flexible data bindings

A **data binding** connects an ontology definition to real data. Bindings describe which source supplies an entity's properties, metrics, instances, or relationships and preserve the mapping between business terminology and source structures. During preview, source options include semantic models, lakehouses, eventhouses, warehouses, SQL databases, mirrored databases, and supported OneLake constructs such as shortcuts, views, and materialized views.

Ontology acts as a virtual semantic and context layer over these sources. Source data remains in the system that owns it, and consuming experiences can query the live bound source rather than copying all data into the ontology.

For more information, see [Data binding in ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data).

[Section titled: Metrics and business rules](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#metrics-and-business-rules)

### Metrics and business rules

**Metrics** give people and agents access to trusted calculations from Power BI semantic models. By carrying source-owned measures into the ontology context, business questions can use established calculations such as revenue, inventory value, or active-customer measures instead of generating new formulas for each consumer.

**Rules** capture business logic in natural language and link it to entities, properties, and relationships. Representing a rule in the ontology makes the same rule context available to multiple consumers, which reduces the need to duplicate business instructions across individual prompts, agents, and applications.

For more information, see [Create and manage business rules in ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-rules).

[Section titled: Namespaces and reuse](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#namespaces-and-reuse)

### Namespaces and reuse

**Namespaces** organize ontology elements into meaningful scopes. They help distinguish and manage concepts across larger models and domains while allowing the ontology to preserve a coherent business vocabulary. For more information, see [Namespaces in ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-namespaces).

**Inheritance** lets authors define a common entity type and extend it for more specialized concepts. **Shared properties** let authors define a property once and reference it across multiple entity types. Together, these capabilities help teams avoid recreating common definitions and maintain consistency as the ontology grows. For more information, see [Model with inheritance in ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-inheritance) and [Reuse shared properties in ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-reuse-properties).

[Section titled: AI-assisted ontology experiences](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#ai-assisted-ontology-experiences)

### AI-assisted ontology experiences

The [ontology agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-agent) supports the ontology lifecycle through natural-language interactions. In the current preview scope, it can use connected Fabric sources to help generate ontology definitions and bindings, answer business questions against ontology context, and propose changes for review. Changes follow a proposal-first model so users can review them before applying them.

Other agent experiences can also consume ontology context. When an agent uses an ontology, it can work with governed entities, relationships, definitions, rules, metrics, and source mappings, helping its responses remain more grounded and consistent across underlying systems. Availability and supported functionality can vary by agent experience. See the documentation for the specific consumer you plan to use.

For more information, see [Use the ontology agent (preview) in Fabric](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-agent).

[Section titled: Real-time exploration](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#real-time-exploration)

### Real-time exploration

You can explore ontology-backed data through entity-focused experiences and Real-Time Dashboards. The ontology supplies definitions and mappings, while the consuming experience executes the query against the relevant source. This separation lets dashboard and agent experiences use the same business context without requiring ontology to duplicate their visualization or query engines.

For more information about ontology as a Real-Time Dashboard source, see [Real-Time Dashboard supported data sources](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-supported-data-sources). For more information about ontology agent, see [Use the ontology agent (preview) in Fabric](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-agent).

[Section titled: Optional graph execution](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#optional-graph-execution)

### Optional graph execution

Ontology defines the business meaning of entities and relationships. **Graph in Microsoft Fabric is an optional execution layer** for scenarios in which the relationship path itself is important, such as multihop traversal, dependency analysis, reachability, or shortest-path questions. Routine lookups, aggregations, metrics, and fresh time-series questions can continue to use their source systems.

An ontology-derived schema graph doesn't load instance data by default. When you need graph execution, you can opt in to materializing the relevant data. This data materialization replaces the earlier framing that presented every ontology as having an automatically materialized instance graph.

For more information, see [Materialize a graph from an ontology (preview)](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-graph).

[Section titled: Lifecycle, interoperability, and governance](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#lifecycle-interoperability-and-governance)

### Lifecycle, interoperability, and governance

Ontology supports named [version history](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-version-history) so authors can create checkpoints, review prior versions, and restore a known state. In the initial experience, you create versions manually, and each version includes identifying information such as date, time, creator, name, and description. Restoring a version replaces the current ontology definition with that saved definition.

Ontology can also [import](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-import-export#import-an-ontology) supported RDF, Turtle, and OWL definitions into an empty ontology item and [export](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-import-export#export-an-ontology) supported ontology definitions in RDF or Turtle formats. Import results identify preserved, automatically adjusted, and unsupported elements so authors can review how an external definition maps to ontology in Fabric.

Fabric workspace and item permissions control access to ontology items. Authoring and querying respect access to bound data, including OneLake security and source-enforced row-level security (RLS), object-level security (OLS), and column-level security (CLS), alongside programmatic access and CI/CD capabilities. For more information, see [Table, column, and row-level security in OneLake](https://learn.microsoft.com/en-us/fabric/onelake/security/table-column-row-security).

[Section titled: Core concepts](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#core-concepts)

## Core concepts

[Section titled: Entity type](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#entity-type)

### Entity type

An **entity type** is the reusable definition of a business concept, such as _Customer_, _Shipment_, _Machine_, or _Store_. It can define a name, description, properties, identifiers, metrics, rules, metadata, and relationships. An entity type represents business meaning independently of any single source table.

[Section titled: Entity instance](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#entity-instance)

### Entity instance

An **entity instance** is a data-backed occurrence of an entity type, such as a particular customer or machine. Consuming experiences resolve instances from an entity type's bindings, then display or query them.

[Section titled: Property](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#property)

### Property

A **property** is a named characteristic of an entity type, such as a customer's email address or a machine's operating state. Properties have data types, and you can map them to fields in one or more bound sources.

[Section titled: Relationship](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#relationship)

### Relationship

A **relationship** defines how two entity types connect, such as _Customer places Order_ or _Machine belongs to Production Line_. Relationships make business connections explicit and reusable by people, applications, agents, and optional graph execution.

[Section titled: Metric](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#metric)

### Metric

A **metric** represents a governed calculation associated with ontology concepts. In the preview experience, metrics originate from DAX measures in a source semantic model and retain their connection to that source.

[Section titled: Rule](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#rule)

### Rule

A **rule** is a natural-language statement of business logic linked to ontology concepts. Rules provide additional operational context that supported consumers can use during reasoning.

[Section titled: Namespace](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#namespace)

### Namespace

A **namespace** provides a scope for organizing and distinguishing ontology elements. Namespaces are especially useful when a model contains concepts owned by multiple domains or teams.

[Section titled: Data binding](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#data-binding)

### Data binding

A **data binding** maps ontology definitions to source data. It identifies the source structures that provide entity properties, instances, metrics, or relationship values and lets consumers work in ontology terminology while using data from the owning system.

[Section titled: Migrate from old experience](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#migrate-from-old-experience)

## Migrate from old experience

The new ontology experience is the default experience for new ontology items.

Note

You can't create new instances of the old ontology experience through the ontology interface in Fabric. It's still possible to create instances of the old experience by using the ontology APIs and CI/CD.

The new ontology experience lays the groundwork for future ontology investments across Microsoft Fabric, as well as related agent and operational intelligence experiences. It enables more flexible business modeling, support for a wider range of data sources, greater reuse of semantic models, enhanced developer tooling, and deeper integration with agents and downstream experiences.

To take advantage of these updates, customers who use the old experience for their ontology items should migrate to the new experience. Use the in-product action to create a copy of your ontology in the new experience. This copy flow preserves the original item while creating a separate new ontology item based on its supported definitions.

[![Screenshot of the banner in the old ontology with a button to create a copy in the new experience.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview/migrate-banner.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview/migrate-banner.png#lightbox)

The new experience item is created with the same entity types, properties and bindings, and relationship types from the original old experience item.

After you create the new experience item, review these elements manually and re-create them if needed:

- Because the new experience copy is a separate item in Fabric, reconnect downstream consumers to the new item. This might include:
  - Agents
  - Dashboards
  - Other integrations
- Recreate [rules](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-rules#migrate-activator-rules-from-ontology-old-experience) and manually set up Activator alerts if you need them.

Your old ontology stays in your workspace and is available until the old experience retires.

[Section titled: Troubleshooting and known issues](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#troubleshooting-and-known-issues)

## Troubleshooting and known issues

For ontology known issues, see [Microsoft Fabric known issues](https://support.fabric.microsoft.com/known-issues/) and search for _ontology_.

For troubleshooting details, see [Troubleshoot ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/resources-troubleshooting).

[Section titled: Next steps](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#next-steps)

## Next steps

- [Prepare your tenant](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings) by enabling the required ontology settings.
- [Create an ontology manually](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology) or [generate one from a Power BI semantic model](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-generate-from-semantic-models).
- [Bind ontology concepts](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data) to your enterprise data.
- Add [metadata](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-add-metadata), [rules](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-rules), [metrics](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-metrics), [inheritance](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-inheritance), [shared properties](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-reuse-properties), and [namespaces](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-namespaces).
- Connect a [supported agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/concepts-agent-integration) or [Real-Time Dashboard](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-supported-data-sources) to consume the ontology context. Or, use the built-in [ontology agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-agent) experience.
- If you have an existing ontology item that was created with the old experience, review the [migration guidance](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#migrate-from-old-experience) and create a copy in the new experience.
- View ontology known issues on the [Microsoft Fabric known issues site](https://support.fabric.microsoft.com/known-issues/) (search for _ontology_), or view [ontology troubleshooting details](https://learn.microsoft.com/en-us/fabric/iq/ontology/resources-troubleshooting).

Reading mode disabled

* * *

## Feedback

Was this page helpful?


YesNoNo

Need help with this topic?


Want to try using Ask Learn to clarify or guide you through this topic?


Ask LearnAsk Learn

Suggest a fix?

* * *

## Additional resources

* * *

- Last updated on 10/16/2026

Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.

Please sign in to use Ask Learn.

[Sign in](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#)
