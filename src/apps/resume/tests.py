# from django.test import Client
# from django.test import TestCase
#
# from apps.resume.views import view_index
#
#
# class Test(TestCase):
#     def setUp(self) -> None:
#         self.cli = Client()
#
#     def test_get(self):
#         resp = self.cli.get("/resume/")
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(len(resp.jinja2), 2)
#         self.assertEqual(
#             [_t.name for _t in resp.jinja2], ["resume/index.html", "base.html"]
#         )
#         self.assertEqual(resp.resolver_match.func, view_index)
