Table of contents Exit editor mode

Ask LearnAsk Learn

Reading modeTable of contents[Read in English](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology)Add to CollectionsAdd to Plans[Edit](https://github.com/MicrosoftDocs/fabric-docs/blob/main/docs/iq/ontology/tutorial-1-create-ontology.md)

* * *

Copy MarkdownPrint

* * *

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#) or changing directories.


Access to this page requires authorization. You can try changing directories.


# Ontology (preview) tutorial part 1: Create an ontology

Feedback

Summarize this article for me


In this step of the tutorial, you create a new ontology (preview) item that represents the Lakeshore Retail scenario. Then you add entity types, data bindings, and relationships to build out the ontology.

Important

This feature is in [preview](https://learn.microsoft.com/en-us/fabric/fundamentals/preview).

[Section titled: Create ontology (preview) item](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#create-ontology-preview-item)

## Create ontology (preview) item

1. In your Fabric workspace, select **\+ New item**. Search for and select the **Ontology (preview)** item.

[![Screenshot of the ontology (preview) item.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/new-ontology.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/new-ontology.png#lightbox)

2. In the **New Ontology** dialog, enter a **Name** of _LakeshoreOntology_. Set the **Location** to your workspace. Select **Create**.


The ontology opens when it's ready.

[![Screenshot of empty ontology in Fabric item.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-blank.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-blank.png#lightbox)

Note

If you see an error that Fabric is unable to create the ontology (preview) item, ensure that all the required settings are enabled for your tenant, as described in the [Tutorial prerequisites](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-0-introduction?pivots=onelake#prerequisites).

Next, create entity types, data bindings, and relationships based on data from your lakehouse tables.

[Section titled: Create entity types and data bindings](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#create-entity-types-and-data-bindings)

## Create entity types and data bindings

First, create entity types. Entity types represent types of objects in a business. After you create the entity types, create their properties by binding source data columns from the _LakeshoreStaticDataLH_ lakehouse tables.

[Section titled: Add base entity type (Location)](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#add-base-entity-type-location)

### Add base entity type (Location)

1. From the top ribbon, select **\+ Add entity type**.

[![Screenshot of adding entity type from the top ribbon.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/add-entity-type.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/add-entity-type.png#lightbox)

2. Enter _Location_ for the entity type name and select **Add Entity Type**.

3. The Location entity type appears on the configuration canvas.

[![Screenshot of the new Location entity type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-entity-type.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-entity-type.png#lightbox)


[Section titled: Bind Location data](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#bind-location-data)

#### Bind Location data

1. On the configuration canvas or the Explorer, select **...** next to the entity name and select **Bind data**.

[![Screenshot of selecting Bind data for Location.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data.png#lightbox)

2. Select **Add** to add a data source.

3. Find the data source in the OneLake catalog. Expand _LakeshoreStaticDataLH_ \> _dbo_ and select the _dimlocations_ table. Confirm with **Select table**.

4. The data source loads.

[![Screenshot of the data source after it is loaded.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data-source.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data-source.png#lightbox)

5. Select **Entity type properties** to see properties of the entity type. The columns from the _dimlocations_ table automatically populate as proposed properties.

[![Screenshot of properties automatically populated on the entity type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data-properties.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data-properties.png#lightbox)

6. Without making any changes to the properties, select **Create** to save the data binding. You see a banner confirming that **Entity type updated successfully**.

7. Select **Cancel** to close the property binding dialog.

8. You see the **Configure** page of the entity type details. This page surfaces information about the entity type, including its properties and data bindings. View your configured data bindings.

[![Screenshot of the data bindings in the Configure page.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data-done.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/location-bind-data-done.png#lightbox)


Now the Location entity type is complete.

[Section titled: Add inherited entity type (Store)](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#add-inherited-entity-type-store)

### Add inherited entity type (Store)

Next, add an inherited entity type. The Store entity inherits from Location, which automatically gives it all of Location's properties.

1. Select **Home** to return to the configuration canvas where you can add new entity types.

[![Screenshot of returning home to the configuration canvas.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/home.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/home.png#lightbox)

2. From the top ribbon, select **\+ Add entity type**.

3. Enter _Store_ for the **Entity type name**. Expand **Additional configuration** and set **Choose entity to inherit from** to _Location_. Select **Add Entity Type**.

[![Screenshot of adding the Store entity type that inherits from Location.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/add-store.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/add-store.png#lightbox)

4. The Store entity type appears on the configuration canvas.

5. Select the Store entity type and select **View Entity Type details**.

[![Screenshot of opening entity type details for the Store entity type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-entity-type-details.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-entity-type-details.png#lightbox)

6. In the **Configure** tab, confirm that the Store entity type already has properties. These properties are inherited from the Location parent, but you still need to bind them to a source.

[![Screenshot of the Store entity type's inherited properties.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-properties-unbound.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-properties-unbound.png#lightbox)


[Section titled: Bind Store data](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#bind-store-data)

#### Bind Store data

1. Select **Manage property bindings** \> **Add binding and properties**.

[![Screenshot of adding binding and properties to the Store entity type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-add-binding.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-add-binding.png#lightbox)

The property binding page opens.

2. **Add** the _LakeshoreStaticDataLH_ \> _dbo_ \> _dimlocations_ table as a data source.

3. Select **Entity type properties**, verify that properties have a populated source column, and select **Create**.

[![Screenshot of source columns in the data binding.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-add-binding-source-column.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-add-binding-source-column.png#lightbox)

4. Select **Cancel** to return to the **Configure** page for the entity type.


Now the Store entity type is complete. Continue to the next section to create the rest of the entity types in the sample scenario.

[Section titled: Add other entity types](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#add-other-entity-types)

### Add other entity types

Use the same steps that you used for the Location and Store entity types to create the entity types described in the following table. Add all of their source columns as properties.

Expand table

| Entity type name | Inherits from | Data source table | Notes |
| --- | --- | --- | --- |
| Distribution Center | Location | _LakeshoreStaticDataLH_ \> _dimlocations_ |  |
| Product |  | _LakeshoreStaticDataLH_ \> _dimproducts_ |  |
| Frozen Product | Product | _LakeshoreStaticDataLH_ \> _dimproducts_ |  |
| Perishable Product | Product | _LakeshoreStaticDataLH_ \> _dimproducts_ |  |
| Inventory |  | _LakeshoreStaticDataLH_ \> _fact\_inventory\_positions_ |  |
| Supplier |  | _LakeshoreStaticDataLH_ \> _dimsuppliers_ |  |
| Shipment |  | _LakeshoreStaticDataLH_ \> _factshipments_ |  |
| Refrigeration Unit |  | _LakeshoreStaticDataLH_ \> _dim\_refrigeration\_units_ |  |
| Refrigeration Telemetry |  | _LakeshoreTelemetryDataEH_ \> _RefrigerationTelemetry_ | This entity type uses the eventhouse table, not a lakehouse table, as its data source. |

When you finish, you see all the entity types listed in the **Explorer** in the configuration canvas.

[![Screenshot of the scenario entity types.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/all-entity-types.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/all-entity-types.png#lightbox)

[Section titled: Add Sale with the ontology agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#add-sale-with-the-ontology-agent)

### Add Sale with the ontology agent

Finally, add one more entity type: Sale. Unlike the other entity types, Sale's source data is in a semantic model and has associated DAX measures. To bind this Sale data without having to recreate it manually, use the ontology agent.

1. Select **Ontology agent** from the top ribbon. The ontology agent opens in **Plan** mode.

[![Screenshot of opening the ontology agent in Plan mode.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-agent.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-agent.png#lightbox)

2. Send the following query: _Create a new entity type called Sale, bound to data in the Sales table from the SalesReport semantic model inside this workspace._

3. The ontology agent reasons and creates a plan for adding the new entity type.

[![Screenshot of the ontology agent's plan for adding the entity type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-agent-plan.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-agent-plan.png#lightbox)

4. Toggle to **Act** mode and send _Apply the entity type plan_.

5. The ontology agent adds the Sale entity type to the canvas.

[![Screenshot of the ontology agent's success message and the Sale entity type added to the canvas.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-agent-sale.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/ontology-agent-sale.png#lightbox)

6. With the new Sale entity type highlighted, select **View Entity Type details**.

7. Verify that **Properties** are populated and bound to the semantic model data source.

[![Screenshot of the Sale entity properties.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/sale-details.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/sale-details.png#lightbox)

8. Scroll down to view the **Metrics** section and verify that two metrics are added. Ontology metrics are based on DAX measures from the semantic model source.

[![Screenshot of the Sale entity metrics with two entries.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/sale-metrics.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/sale-metrics.png#lightbox)


Now you have all entity types for the scenario created and bound to source data.

[Section titled: Create relationship types](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#create-relationship-types)

## Create relationship types

Next, create relationship types between the entity types to represent contextual connections in your data.

[Section titled: Store operates Refrigeration Unit](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#store-operates-refrigeration-unit)

### Store operates Refrigeration Unit

1. Select the Store entity type from the **Explorer**.

2. Select **Add relationship** from the menu ribbon or the Explorer, or **Add relationship type** from the entity on the configuration canvas.

[![Screenshot of adding a relationship type.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-add-relationship.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/store-add-relationship.png#lightbox)

3. Enter the following relationship type details and select **Create**.


1. **Relationship type name**: _operates_
2. **Origin entity type**: _Store_
3. **Target entity type**: _Refrigeration Unit_

[![Screenshot of entering relationship type details.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/add-new-relationship.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/add-new-relationship.png#lightbox)

4. The relationship appears on the semantic canvas. Select it to open the relationship details configuration.

5. Observe the sections of the configuration page:


   - **Origin entity type**: Lists details of the origin entity type (Store)
   - **Relationship**: Sets details of the relationship type ( _operates_)
   - **Target entity type**: Lists details of the target entity type (Refrigeration Unit)

[![Screenshot of the relationship type configuration.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/relationship-configuration.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/relationship-configuration.png#lightbox)

6. In the **Origin entity type** section, expand **Property** and select `LocationId`.

In the **Target entity type** section, expand **Property** and select `StoreId`. These fields indicate that the `LocationId` on a Store can be matched to the `StoreId` on a Refrigeration Unit to relate them to each other.

[![Screenshot of the details filled out in the relationship type configuration.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/relationship-configuration-done.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/relationship-configuration-done.png#lightbox)

7. **Save** the relationship type. You see a banner confirming that the ontology **Successfully updated the relationship type**. Select **Cancel** to close the configuration options.

8. You see the **Configure** page for the Store entity type, where the new relationship is visible in the **Relationships** section.

[![Screenshot of the relationship type in the Configure page.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/relationship-done.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/relationship-done.png#lightbox)


Now the first relationship is complete. Continue to the next section to create the rest of the relationship types in the sample scenario.

[Section titled: Add other relationship types](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#add-other-relationship-types)

### Add other relationship types

Select **Home** to return to the configuration canvas where you can add new relationship types.

Follow the same steps that you used for the first relationship type to create the relationship types described in the following table.

Expand table

| Relationship type name | Origin entity type (Property) | Target entity type (Property) |
| --- | --- | --- |
| _operates_ | Store (`LocationId`) | Refrigeration Unit (`StoreId`) |
| _deliversTo_ | Shipment (`ToStoreId`) | Store (`LocationId`) |
| _occursAt_ | Sale (`StoreId`) | Store (`LocationId`) |
| _stockedAt_ | Inventory (`StoreId`) | Store (`LocationId`) |
| _originatesAt_ | Shipment (`FromLocationId`) | Distribution Center (`LocationId`) |
| _forProduct_ | Sale (`ProductId`) | Product (`ProductId`) |
| _stockedAt_ | Product (`ProductId`) | Inventory (`ProductId`) |
| _suppliedBy_ | Product (`SupplierId`) | Supplier (`SupplierId`) |
| _contains_ | Shipment (`ProductId`) | Product (`ProductId`) |
| _hasTelemetryReading_ | Refrigeration Unit (`UnitId`) | Refrigeration Telemetry (`UnitId`) |

When you're done, the relationship types are visible on the configuration canvas.

[![Screenshot of the scenario relationship types.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/all-relationship-types.png)](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/tutorial-1-create-ontology/all-relationship-types.png#lightbox)

[Section titled: Next steps](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#next-steps)

## Next steps

In this step, you created an ontology (preview) item and populated it with entity types, their properties, and relationship types between them. Next, enrich the entity types with more detail.

Next, continue to [Enrich the ontology with additional data](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-2-enrich-ontology).

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

- Last updated on 09/29/2026

Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.

Please sign in to use Ask Learn.

[Sign in](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology#)
