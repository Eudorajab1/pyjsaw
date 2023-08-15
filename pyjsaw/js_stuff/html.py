# flake8: noqa E701

class Tag:
    ...

class MetaTag:
    ...

class VoidTag:
    ...


class HTMLText(MetaTag): ...
class Text(MetaTag): ...

class Figure(Tag): ...
class Small(Tag): ...

class Html(Tag): ...
class Head(Tag): ...
class Meta(VoidTag): ...
class Title(Tag): ...
class Style(Tag): ...
class Link(VoidTag): ...
class Script(Tag): ...


class Body(Tag): ...

class Article(Tag): ...
class Aside(Tag): ...
class Header(Tag): ...
class Main(Tag): ...
class Nav(Tag): ...
class Section(Tag): ...
class Footer(Tag): ...
class Canvas(Tag): ...

class H1(Tag): ...
class H2(Tag): ...
class H3(Tag): ...
class H4(Tag): ...
class H5(Tag): ...
class H6(Tag): ...


class A(Tag): ...
class B(Tag): ...
class P(Tag): ...
class I(Tag): ...
class Hr(Tag): ...

class Div(Tag): ...
class Span(Tag): ...
class Em(Tag): ...
class Img(VoidTag): ...

class Pre(Tag): ...
class Code(Tag): ...


class Form(Tag): ...
class Fieldset(Tag): ...
class Legend(Tag): ...
class Label(Tag): ...
class Input(VoidTag): ...
class Datalist(Tag): ...
class Select(Tag): ...
class Option(Tag): ...
class Optgroup(Tag): ...
class Textarea(Tag): ...
class Progress(Tag): ...
class Meter(Tag): ...
class Button(Tag): ...


class OL(Tag): ...
class UL(Tag): ...
class LI(Tag): ...


class Table(Tag): ...
class Caption(Tag): ...
class Colgroup(Tag): ...
class Col(Tag): ...
class THead(Tag): ...
class TBody(Tag): ...
class TFoot(Tag): ...
class TH(Tag): ...
class TR(Tag): ...
class TD(Tag): ...


class Frame(Tag): ...
