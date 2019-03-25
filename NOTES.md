### Case and Handler function naming
.go() should be renamed on the UseCases and Handlers, the name should be short but also
note that it is not to be called directly.  Perhaps preceding with an underscore

### Model / Entity naming
**Model**, has baggage due to use within FlaskSQLAlchemy.
**Entity**, has different spelling for plural (Entities) which I want to avoid due to annoyance with
current codebase and use of objects that follow this naming (Company, Companies for example)

### DTO directions
Wondering if DTO's should be passed up the chain to Handlers as well as down the chain to Repos.  
Alternatively to this could have DTOs down to Repos, and Domain Models/Entities up/out to handlers.
At this point it is also unclear how different a DTO is from a Model/Entity.
