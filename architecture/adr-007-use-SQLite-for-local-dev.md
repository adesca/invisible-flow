# Use SQLite for local development

## Status

accepted

## Context

Allows local development without having the need for a server deployed externally

## Decision

Use SQLite for local development

## Consequences
- ~~Must keep local instance schemas up to date~~
    - SQLAlchemy does this for us
- ~~Falls on the developer to maintain~~
    - SQLAlchemy does this for us
- No need for a server deployed or to maintain
- Better than using personal google cloud sql instance due to permissions on project dev rolloffs
- ~~SQLite schema/db exports are directly importable to PostgreSQL~~
    - SQLAlchemy does this for us
