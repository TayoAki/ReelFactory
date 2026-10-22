# Fabric visual identity evidence and video theme

Checked October 22, 2026. Use `theme.json` for this project's Fabric video palette.

| Role | Color | Evidence |
|---|---|---|
| Dark teal | `#225B62` | Observed primary/button color on the official Fabric homepage |
| Emerald | `#117865` | Exact stop in the official Fabric color SVG |
| Teal | `#177E71` | Exact stop in the official Fabric color SVG |
| Deep teal | `#063D3B` | Exact stop in the official Fabric color SVG |
| Light mint surfaces | `#F0FAF6` → `#D3EFE5` | Our derived editorial tints, not official brand tokens |
| Focal border | `#AED8CB` | Our derived editorial tint |
| Text | `#172B2A` | Our readable neutral choice |

The official SVG has multiple gradients, not one universal “Fabric hex.” Homepage extraction is observed styling, not proof of a comprehensive brand standard. The homepage uses Segoe UI Variable; we retain the user's preferred editorial serif as a video design choice, not an official Microsoft typography claim.

`fabric-official.svg` was downloaded unchanged from Microsoft's `@fabric-msft/svg-icons` package version 11.1.0, path `svg/fabric_32_color.svg`. The PNG is a direct SVG rasterization for image-generation reference, with no creative alteration. Product icon terms: https://learn.microsoft.com/en-us/fabric/fundamentals/icons . Permitted for architectural diagrams, training and documentation; do not distort or recolor official product icons. Generic Store/Refrigeration Unit symbols are explanatory illustrations, not Fabric product marks.

Sources:
- https://www.microsoft.com/en-us/microsoft-fabric
- https://learn.microsoft.com/en-us/fabric/fundamentals/icons
- https://registry.npmjs.org/@fabric-msft/svg-icons/-/svg-icons-11.1.0.tgz
- https://aka.ms/fabricux (current official UX System)

The old download ZIP and old Azure Static Apps UX link returned 404. The current UX site's color gallery did not render through retrieval. Consequently, these values are documented as homepage/icon observations and project tints, not verified UX alias tokens. `research.json` retains retrieval evidence.
