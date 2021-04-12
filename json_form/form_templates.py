TEST_FORM = """
<div id="app"></div>
<script src="https://unpkg.com/@rjsf/core/dist/react-jsonschema-form.js" crossorigin></script>
<script>
const Form = JSONSchemaForm.default;
const schema={
  title: "Test form",
  type: "string"
};

const uiSchema = {
  classNames: "custom-css-class"
};

ReactDOM.render((
  < Form schema={schema} uiSchema={uiSchema} />
), document.getElementById("app"));
</script>
"""


SIMPLE_FORM = """
<div>Hi</div>
<div id="pydantic_schema_form"></div>
<!-- Load React. -->
<!-- Note: when deploying, replace "development.js" with "production.min.js". -->
<script src="https://unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
<!-- page scripts-->
<script src="https://unpkg.com/@rjsf/core/dist/react-jsonschema-form.js" crossorigin></script>
<script>
  const Form = JSONSchemaForm.default;
  const schema={{pydantic_schema_form.schema}};
  
    
  const log = type => console.log.bind(console, type);

  ReactDOM.render( /*#__PURE__*/
    React.createElement(Form, {
      schema: schema,
      
      onChange: log("changed"),
      onSubmit: log("submitted"),
      onError: log("errors")
    }),
    document.getElementById("pydantic_schema_form"));
</script>
      """

FULL_PAGE = """
    <!DOCTYPE html>
<html lang="en">
<head>
  <title>Form Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>Example Form Page</h1>
  <p>Just pass the JSON Schema to render the form</p> 
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <div id="pydantic_schema_form"></div>
<!-- Load React. -->
<!-- Note: when deploying, replace "development.js" with "production.min.js". -->
<script src="https://unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
<!-- page scripts-->
<script src="https://unpkg.com/@rjsf/core/dist/react-jsonschema-form.js" crossorigin></script>
<script>
  const Form = JSONSchemaForm.default;
  const schema={{pydantic_schema_form.schema}}
  
    
  const log = type => console.log.bind(console, type);

  ReactDOM.render( /*#__PURE__*/
    React.createElement(Form, {
      schema: schema,
      
      onChange: log("changed"),
      onSubmit: log("submitted"),
      onError: log("errors")
    }),
    document.getElementById("pydantic_schema_form"));
</script>
    </div>
  </div>
</div>

</body>
</html>
    """
FULL_PAGE_TWO = """
    <!DOCTYPE html>
<html lang="en">
<head>
  <title>Form Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>Example Form Page</h1>
  <p>Just pass the JSON Schema to render the form</p> 
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <div id="app"> </div>
<!-- Load React. -->
<!-- Note: when deploying, replace "development.js" with "production.min.js". -->
<script src="https://unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
<!-- page scripts-->
<script src="https://unpkg.com/@rjsf/core/dist/react-jsonschema-form.js" crossorigin></script>
<script>
const Form = JSONSchemaForm.default;
const schema = {{pydantic_schema_form.schema|safe}};
const uiSchema={{pydantic_schema_form.uiSchema|safe}};
const log = (type) => console.log.bind(console, type);

ReactDOM.render( /*#__PURE__*/
  React.createElement(Form, {
    schema: schema,
    uiSchema: uiSchema,
    onChange: log("changed"),
    onSubmit: log("submitted"),
    onError: log("errors")
  }),
  document.getElementById("app"));
</script>
    </div>
  </div>
</div>
</body>
</html>
"""
