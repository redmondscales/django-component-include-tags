# Django Component Include Tags
This package includes a simple extention to the built-in include tag that enables component-style templating.
## Installation
Install the package using pip
```bash
pip install django-component-include-tags
```
Add the app to your INSTALLED_APPS in your settings.py
```python
INSTALLED_APPS = [
    ...
    'component_include_tags',
    ...
]
```
If you want the component tags available globally
```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'builtins': [
                ...
                'component_include_tags.templatetags.components',
                ...
            ],
        },
        ...
    },
]
```
## Usage
The syntax is the same as an include tag but it allows you to define sections and pass html from your current template into into the included template.

For example, with a component template like this:
```html
# app/components/card.html
<div class="card">
    {{body}}
    <div class="footer">
        {{footer}}
    </div>
</div>
```
You can render the card component in your template like this
```html
{% load components %}
{% component 'myapp/components/card.html' %}
    <div>Card Body Content here</div>

    {% section footer %}
        <div>Card Some Footer Content here</div>
    {% endsection %}

{% endcomponent %}
```
The above will render the following html:
```html
<div class="card">
    Card Body Content here

    <div class="footer">
        <div>Card Some Footer Content here</div>
    </div>
</div>
```
## Wrapping Sections
You may only want to render some layout html if a section has content. Say for example you have a card component with a body and footer section, but you only want to render a divider and a darker background behind the footer area if you provide footer content.

For this you can also utilise the "wrapper" tag to conditional render html around your sections only if they have content.

If we modify the card component and add a wrapper tag around where the footer content will go. The surrounding layout html will only be rendered if the footer section has content, meaning you wont have an empty bordered footer section if you dont need it.
```html
{% load components %}
<div class="card">
    {{body}}
    {% wrapper footer %}
        # the wrapping div.footer is only rendered
        # if the footer template variable has content
        <div class="footer">
            {{footer}}
        </div>
    {% endwrapper %}
</div>
```
The wrapper tag looks for the template variable using the name you pass in, in this instance {% wrapper footer %} will look for the {{footer}} template variable.

The {{footer}} template variable is populated by the content of the {% section footer %} tag from the parent template that is using the component.

If you exclude the footer section, this will be rendered:
```html
<div class="card">
    Card Body Content here
</div>
```
## Extra Context
Just as you can with {% include %}, you can pass additional context data to the component template.

If we modiy the card component to include a title variable:
```html
# app/components/card.html
<div class="card">
    <div class="title">{{title}}</div>
    {{body}}
    <div class="footer">
        {{footer}}
    </div>
</div>
```
```html
{% component_include 'myapp/components/card.html' title="My Card Title" %}
    <div>Card Body Content here</div>

    {% section footer %}
        <div>Card Some Footer Content here</div>
    {% endsection %}

{% endcomponent %}
```
This will be rendered
```html
<div class="card">
    <div class="title">My Card Title</div>
    Card Body Content here

    <div class="footer">
        Card Some Footer Content here
    </div>
</div>
```
## Why?
It allows you to turn any django template into a component letting you to drop rendered html from your main template into it. The include tag only allows you to pass variables, this allows you to pass html.
```html
{% include 'components/card.html' body="can only pass strings" %}

vs

{% component 'components/card.html' %}
    {% section body %}
        <h2>Can pass whatver html you want here</h2>
        <div>{{some_context_variable}}</div>
    {% endsection %}
{% endcomponent %}
```