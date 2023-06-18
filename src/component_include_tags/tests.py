from django.test import TestCase

# Create your tests here.
from django.template.loader import render_to_string


def flatten_html(html):
    return html.strip().replace("\n", "").replace(" ", "")


class ComponentIncludeTagTestCase(TestCase):
    def test_renders_body_without_section_tags(self):
        rendered = render_to_string(
            "no_section_tags.html",
        )
        self.assertEqual(
            flatten_html(rendered),
            flatten_html(
                """<div>
                <div>
                <h4>Body</h4>
                </div>
            </div>"""
            ),
        )

    def test_renders_section_tags(self):
        rendered = render_to_string(
            "index.html",
        )
        self.assertEqual(
            flatten_html(rendered),
            flatten_html(
                """<div>
                <div>
                <h1>Header</h1>
                Header Text
                </div>
                <div>
                <h4>Body</h4>
                </div>
                <div>
                <h2>Footer</h2>
                Footer Text
                </div>
            </div>"""
            ),
        )
