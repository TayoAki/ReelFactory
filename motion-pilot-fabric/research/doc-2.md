Table of contents Exit editor mode

Ask LearnAsk Learn

Reading modeTable of contents[Read in English](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data)Add to CollectionsAdd to Plans[Edit](https://github.com/MicrosoftDocs/fabric-docs/blob/main/docs/iq/ontology/how-to-bind-data.md)

* * *

Copy MarkdownPrint

* * *

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#) or changing directories.


Access to this page requires authorization. You can try changing directories.


# Data binding in ontology (preview)

Feedback

Summarize this article for me


Data binding in ontology (preview) connects the schema of entity types, relationship types, and properties to concrete data sources that drive enterprise operations and analytics.

Important

This feature is in [preview](https://learn.microsoft.com/en-us/fabric/fundamentals/preview).

By using data binding, you can:

- Integrate data into a semantic layer without copying source data
- Enrich entity types with up-to-date contextual information from batch and real-time sources
- Provide a semantic backbone for AI agents and automation to support reasoning, decision-making, and actions across the enterprise

[Section titled: Prerequisites](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#prerequisites)

## Prerequisites

Before binding data to your ontology, make sure you have the following prerequisites:

- A [Fabric workspace](https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](https://learn.microsoft.com/en-us/fabric/enterprise/licenses#capacity).
- **Users can create ontology (preview) items** and **Users can create Fabric items** [enabled on your Fabric tenant](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings).
- An ontology (preview) item with [entity types](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data) created.
- Data that you prepared according to these guidelines:
  - The data is organized and has gone through any necessary ETL required by your business. It contains all the information required to model it. For more information, see [Core concept: Data binding](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview#data-binding).
  - The data is in Microsoft Fabric. Supported sources include eventhouse, KQL database, lakehouse, mirrored database, semantic model, SQL database, or warehouse.
    - For semantic models, you need both [Read and Build permissions](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-permissions#what-are-the-semantic-model-permissions) to bind the data to an ontology.

[Section titled: Add data binding](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#add-data-binding)

## Add data binding

1. You can start a data binding from either the Home configuration canvas or the **Configure** tab of the entity type details.

On the Home configuration canvas, select **...** next to an entity type name to open its options menu and select **Bind data**.

[![Screenshot of starting a data binding from the configuration canvas.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-canvas.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-canvas.png#lightbox)

On the **Configure** page, select **Manage property bindings** \> **Add properties** or **Add binding and properties**. You can also select the **Add properties from data** button if the entity type has no properties yet.

[![Screenshot of adding a new data binding to the entity type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-add.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-add.png#lightbox)

2. The **Property binding** page opens. Select **Add** to add a data source.

[![Screenshot of adding a data source.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/add-data-source.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/add-data-source.png#lightbox)

3. Select your data source table from the OneLake catalog.

[![Screenshot of the data source selection.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-select-table.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-select-table.png#lightbox)

4. The data source loads.

[![Screenshot of the data source after it is loaded.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/data-source-loaded.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/data-source-loaded.png#lightbox)

5. Select **Entity type properties** to see properties of the entity type. The columns from the source table automatically populate as proposed properties.

[![Screenshot of the populated properties.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/entity-type-properties.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/entity-type-properties.png#lightbox)

6. In the **Properties** section, add, rename, or delete properties as needed. Property names can match the source column names or be different. If you have existing properties defined on the entity type, you can select their names from the dropdown menu.

7. When you finish configuring properties, select **Create** to save the data binding. You see a banner confirming that **Entity type updated successfully**.

8. Close the property binding page by selecting **Cancel**. Closing the binding page returns you to the **Configure** page.

9. In the **Configure** page, verify the bindings by reviewing the properties in the **Properties** pane and confirming that they're bound to the correct data sources.

[![Screenshot of the data bindings in the Configure page.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-complete.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-complete.png#lightbox)


[Section titled: Add more data bindings](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#add-more-data-bindings)

### Add more data bindings

Follow these steps to add more bindings after the first binding is created.

1. In the **Configure** page, expand **Manage property bindings** and select **Add binding and properties** again to reopen the binding configuration.

2. On the **Entity type properties** page, select **Add** and select your data table from the OneLake catalog. The system adds the new data source as a secondary data source.

3. The data source loads and asks you to define the relationship between the primary and secondary data source. Select the common column from each table that allows them to relate to each other. Select **Save** to save your progress.

[![Screenshot of defining the data source relationship.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-time-series-relationship.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-time-series-relationship.png#lightbox)

4. Select **Entity type properties**. The system automatically adds all the columns from the new table to the property list, where they appear alongside any properties that you added to the entity previously. If any columns exist in both source tables with the same name, the system adds a _\_2_ suffix to the default property names of the columns from the new data source. Make any changes as needed and **Save** the entity type when you're done.

5. Confirm that the entity type updated successfully, then select **Cancel** to close the configuration options.

6. Back in the **Configure** page, verify the new properties and their binding to the data source.

[![Screenshot of all the data bindings in the Configure page.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-time-series-complete.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/bind-data-time-series-complete.png#lightbox)


[Section titled: Edit or delete data binding](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#edit-or-delete-data-binding)

## Edit or delete data binding

To edit or delete data bindings, start in the **Configure** page. Select **Manage property bindings** \> **\+ Add binding and properties**.

[![Screenshot of the manage bindings options.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/manage-bindings.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/manage-bindings.png#lightbox)

The configuration page reopens, where you can edit binding details or delete binding data sources.

Note

To see updates from upstream data sources, such as new rows, you need to manually refresh the ontology item. For more information, see [refresh the graph model](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-ontology-graph#refresh-the-graph-model).

[Section titled: Supported data source types](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#supported-data-source-types)

## Supported data source types

The following data source types support data binding in ontology (preview):

- Eventhouse
- KQL database
- Lakehouse
- Mirrored database
- Semantic model
- SQL database
- Warehouse

[![Screenshot of the data source types in the OneLake catalog.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/source-types.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/how-to-bind-data/source-types.png#lightbox)

[Section titled: Supported property types](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#supported-property-types)

## Supported property types

The following table lists the supported property types for data that you can bind to properties in ontology (preview).

Expand table

| Ontology property value type | Supported lakehouse types | Supported eventhouse types |
| --- | --- | --- |
| integer | tinyint, smallint, bigint, integer, long, short | int, long |
| boolean | boolean | bool |
| datetime | datetime, date, timestamp | datetime |
| double | double, decimal, float | decimal, real |
| string | char, decimal(p, s), string, array, binary, binary16, byte, map, object, struct, timestampint64, timestamp\_ntz | dynamic, string, guid, timespan |

The following table shows supported source column value types that you can use for the timestamp selection in a time series binding.

Expand table

| Ontology configuration | Lakehouse and eventhouse source column value type |
| --- | --- |
| Timestamp | datetime, date, timestamp |

The following table shows supported property types that you can use as the entity type key.

Expand table

| Ontology configuration | Ontology property value type |
| --- | --- |
| Entity type key | string, integer |

If your data contains other data types, perform ETL to convert the data to one of the supported types before bringing the data to ontology.

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

- Last updated on 10/21/2026

Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.

Please sign in to use Ask Learn.

[Sign in](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data#)
