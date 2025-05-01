


> Written with [StackEdit](https://stackedit.io/).## Extremely Complex Regular Expressions

1.  **RFC 5322 Email Validation (Full Compliance)**

```
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

```

2.  **RFC 5322 Email with Folding Whitespace**

```
((([\t ]*\r\n)?[\t ]+)?[-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*(([\t ]*\r\n)?[\t ]+)?|(([\t ]*\r\n)?[\t ]+)?"(((([\t ]*\r\n)?[\t ]+)?([]!#-[^-~]|(\\[\t -~])))+(([\t ]*\r\n)?[\t ]+)?|(([\t ]*\r\n)?[\t ]+)?)"(([\t ]*\r\n)?[\t ]+)?)@((([\t ]*\r\n)?[\t ]+)?[-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*(([\t ]*\r\n)?[\t ]+)?|(([\t ]*\r\n)?[\t ]+)?\[((([\t ]*\r\n)?[\t ]+)?[!-Z^-~])*(([\t ]*\r\n)?[\t ]+)?](([\t ]*\r\n)?[\t ]+)?)

```

3.  **HTML Tag Parser (Notorious for causing ReDoS)**

```
<([a-z]+)([^<]+)*(?:>(.*)</\1>|\s+/>)

```

4.  **URL Validation (Complex Version)**

```
(?:(?:https?|ftp):\/\/)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/[^\s]*)?

```

5.  **Password Strength Validation (With Multiple Conditions)**

```
(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}

```

6.  **Credit Card Number Validation (All Major Types)**

```
(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})

```

7.  **IPv6 Address Validation**

```
(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))

```

8.  **Date Validation (Multiple Formats)**

```
(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})

```

9.  **Phone Number Validation (International)**

```
(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?

```

10.  **Nested Parentheses Matching (Causes Catastrophic Backtracking)**

```
\(([^()]*|\([^()]*\))*\)

```

11.  **Multiple HTML Tag Matcher**

```
<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>

```

12.  **Windows File Path Validation**

```
(?:[a-zA-Z]:|\\\\[a-zA-Z0-9_.$]+\\[a-zA-Z0-9_.$]+)\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*

```

13.  **JSON Parser (Simplified but Still Complex)**

```
"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*"|[-+]?(?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?|null|true|false|(?:\{(?:[^"{}]|"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*":(?:[^,{}]|,(?=[^{}]))*)*\}|\[(?:[^"[\]]|"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*"|[-+]?(?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?|null|true|false|(?:\{(?:[^"{}]|"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*":(?:[^,{}]|,(?=[^{}]))*)*\}|\[(?:(?:[^"[\]]|"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*"|[-+]?(?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?|null|true|false|(?:\{(?:[^"{}]|"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*":(?:[^,{}]|,(?=[^{}]))*)*\}|\[(?:[^"[\]]|"(?:[^"\\]|\\["\\\/bfnrt]|\\u[0-9a-fA-F]{4})*"|[-+]?(?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?|null|true|false)*\]))*\]))*\]

```

14.  **Multiline Comment Extraction**

```
/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/

```

15.  **ISBN-13 Validation**

```
(?:ISBN(?:-13)?:?\ )?(?=[0-9]{13}$|(?=(?:[0-9]+[-\ ]){4})[-\ 0-9]{17}$)97[89][-\ ]?[0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9]

```

16.  **Windows Registry Path Parser**

```
HKEY_(?:LOCAL_MACHINE|CURRENT_USER|CLASSES_ROOT|USERS|CURRENT_CONFIG)\\(?:[a-zA-Z0-9_]+\\)*[a-zA-Z0-9_]*

```

17.  **Multi-part MIME Message Boundary Extractor**

```
(?:Content-Type:\s*multipart\/[^;]+;\s*boundary=)(?:(?:"([^"\\]*(?:\\.[^"\\]*)*)")|(?:([^;\s]+)))

```

18.  **Complex LaTeX Math Expression**

```
\\begin\{(?:equation|align|gather|multline)[*]?\}(?:\s*\\label\{[^}]*\})?\s*(?:(?:\\[a-zA-Z]+(?:\[(?:[^][]|\[[^]]*\])*\])?(?:\{(?:[^{}]|\{[^{}]*\})*\})?)|[^\\]|\\[^a-zA-Z])*\\end\{(?:equation|align|gather|multline)[*]?\}

```

19.  **YAML Front Matter in Markdown**

```
(?:[\r\n]|^)---[\r\n](?:(?:[ \t]*[a-zA-Z0-9_-]+[ \t]*:[ \t]*(?:(?:.+?)[ \t]*[\r\n]+|(?:\[[^\]]*\]|\{[^}]*\})[ \t]*[\r\n]+)))*[ \t]*---[ \t]*[\r\n]

```

20.  **Advanced IPv6 Address**

```
(?:(?:[0-9a-fA-F]{1,4}:){6}|::(?:[0-9a-fA-F]{1,4}:){5}|(?:[0-9a-fA-F]{1,4})?::(?:[0-9a-fA-F]{1,4}:){4}|(?:(?:[0-9a-fA-F]{1,4}:){0,1}[0-9a-fA-F]{1,4})?::(?:[0-9a-fA-F]{1,4}:){3}|(?:(?:[0-9a-fA-F]{1,4}:){0,2}[0-9a-fA-F]{1,4})?::(?:[0-9a-fA-F]{1,4}:){2}|(?:(?:[0-9a-fA-F]{1,4}:){0,3}[0-9a-fA-F]{1,4})?::[0-9a-fA-F]{1,4}:|(?:(?:[0-9a-fA-F]{1,4}:){0,4}[0-9a-fA-F]{1,4})?::)(?:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:[0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4})?::[0-9a-fA-F]{1,4}|(?:(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4})?::

```

21.  **Apache Access Log Parser**

```
(\S+)\s+(\S+)\s+(\S+)\s+\[([^:]+):(\d+:\d+:\d+)\s+([^\]]+)\]\s+"([A-Z]+)\s+(.+?)\s+HTTP\/(\d\.\d)"\s+(\d{3})\s+(\d+|-)\s+"([^"]*)"\s+"([^"]*)"

```

22.  **Python Multiline Triple-Quoted String**

```
(?:[uUbB]|[uU][bB]|[bB][uU])?[rR]?(?:'''(?:[^'\\]|\\[\s\S]|'(?!''))*'''|"""(?:[^"\\]|\\[\s\S]|"(?!""))*""")

```

23.  **Nested Balancing Groups Parser**

```
((?>\((?:[^()]|(?1))*\))|(?>\[(?:[^\[\]]|(?1))*\])|(?>\{(?:[^{}]|(?1))*\})|<(?:[^<>]|(?1))*>)

```

24.  **Complex Data URI Parser**

```
data:(?:(?:image|video|audio|application|text|message|multipart)\/[a-zA-Z0-9.+-]+)?(?:;(?:charset|base64|name)=[a-zA-Z0-9-]+)*,(?:(?:[a-zA-Z0-9!#$&'*+.^_`|~-]|%[0-9A-F]{2})*|(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)

```

25.  **PEM Certificate Parser**

```
-----BEGIN (?:CERTIFICATE|PRIVATE KEY|PUBLIC KEY|RSA PRIVATE KEY|DSA PRIVATE KEY|EC PRIVATE KEY|CERTIFICATE REQUEST|NEW CERTIFICATE REQUEST|X509 CRL)-----(?:[A-Za-z0-9+/=\s]+)-----END (?:CERTIFICATE|PRIVATE KEY|PUBLIC KEY|RSA PRIVATE KEY|DSA PRIVATE KEY|EC PRIVATE KEY|CERTIFICATE REQUEST|NEW CERTIFICATE REQUEST|X509 CRL)-----

```

26.  **Complex Dockerfile Command Parser**

```
(?:FROM|RUN|CMD|LABEL|MAINTAINER|EXPOSE|ENV|ADD|COPY|ENTRYPOINT|VOLUME|USER|WORKDIR|ARG|ONBUILD|STOPSIGNAL|HEALTHCHECK|SHELL)\s+(?:--\S+=\S+\s+)*(?:(?:[^\s\\]|\\.)+\s*(?:(?:\\\s*[\r\n]\s*)?(?:[^\s\\]|\\.)+\s*)*|(?:"(?:[^"\\]|\\.)*")\s*(?:(?:\\\s*[\r\n]\s*)?(?:"(?:[^"\\]|\\.)*")\s*)*)

```

27.  **CSS Selector with Attributes and Pseudo-classes**

```
(?:(?:[a-zA-Z_]|[^\x00-\x7F])(?:[a-zA-Z0-9_-]|[^\x00-\x7F])*|[*])(?:\[(?:[a-zA-Z_]|[^\x00-\x7F])(?:[a-zA-Z0-9_-]|[^\x00-\x7F])*(?:(?:[~|^$*])?=(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^\[\]'"`,\s]*))?\])*(?::(?:not|has|is|where|nth-child|nth-last-child|nth-of-type|nth-last-of-type|active|any-link|autofill|blank|checked|current|default|defined|disabled|empty|enabled|first-child|first-of-type|focus|focus-visible|focus-within|fullscreen|future|host|host-context|hover|indeterminate|in-range|invalid|last-child|last-of-type|link|local-link|modal|only-child|only-of-type|optional|out-of-range|past|paused|picture-in-picture|placeholder-shown|playing|read-only|read-write|required|scope|target|target-within|user-invalid|valid|visited)(?:\((?:[^)(]|\([^)(]*\))*\))?)*(?:\s*(?:[>+~]|[,\s])\s*(?:(?:[a-zA-Z_]|[^\x00-\x7F])(?:[a-zA-Z0-9_-]|[^\x00-\x7F])*|[*])(?:\[(?:[a-zA-Z_]|[^\x00-\x7F])(?:[a-zA-Z0-9_-]|[^\x00-\x7F])*(?:(?:[~|^$*])?=(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^\[\]'"`,\s]*))?\])*(?::(?:not|has|is|where|nth-child|nth-last-child|nth-of-type|nth-last-of-type|active|any-link|autofill|blank|checked|current|default|defined|disabled|empty|enabled|first-child|first-of-type|focus|focus-visible|focus-within|fullscreen|future|host|host-context|hover|indeterminate|in-range|invalid|last-child|last-of-type|link|local-link|modal|only-child|only-of-type|optional|out-of-range|past|paused|picture-in-picture|placeholder-shown|playing|read-only|read-write|required|scope|target|target-within|user-invalid|valid|visited)(?:\((?:[^)(]|\([^)(]*\))*\))?)*)*

```

28.  **Complex URL Query Parameters Parser**

```
(?:[?&])(?:[a-zA-Z0-9_\-%]+)(?:=(?:[a-zA-Z0-9_\-%]+|(?:%[0-9A-Fa-f]{2})+|(?:"(?:[^"\\]|\\.)*")|(?:'(?:[^'\\]|\\.)*')|(?:\[(?:[^\[\]\\]|\\.)*\])|(?:\{(?:[^{}\\]|\\.)*\})))?(?:&(?:[a-zA-Z0-9_\-%]+)(?:=(?:[a-zA-Z0-9_\-%]+|(?:%[0-9A-Fa-f]{2})+|(?:"(?:[^"\\]|\\.)*")|(?:'(?:[^'\\]|\\.)*')|(?:\[(?:[^\[\]\\]|\\.)*\])|(?:\{(?:[^{}\\]|\\.)*\})))?)*

```

29.  **Ruby Heredoc Syntax Parser**

```
<<[-~]?(?:(?:'([^']*)(?:(?<=\\)'|[^\\'])*')|(?:"([^"]*)(?:(?<=\\)"|[^\\"])*")|([a-zA-Z0-9_]+))\s*(?:.*\n(?:(?:(?!\1|\2|\3).*\n)*)(?:\1|\2|\3))

```

30.  **PCRE Named Capturing Groups Extractor**

```
\(\?(?:P?<([^>]+)>|'([^']+)'|<([^>]+)>)(?:[^()]|\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))*\)

```

31.  **Comprehensive Unicode Property Regex**

```
\\[pP]\{(?:(?:Is|gc|General_Category)=)?(?:L|Letter|Lu|Uppercase_Letter|Ll|Lowercase_Letter|Lt|Titlecase_Letter|Lm|Modifier_Letter|Lo|Other_Letter|M|Mark|Mn|Nonspacing_Mark|Mc|Spacing_Mark|Me|Enclosing_Mark|N|Number|Nd|Decimal_Number|Nl|Letter_Number|No|Other_Number|P|Punctuation|Pc|Connector_Punctuation|Pd|Dash_Punctuation|Ps|Open_Punctuation|Pe|Close_Punctuation|Pi|Initial_Punctuation|Pf|Final_Punctuation|Po|Other_Punctuation|S|Symbol|Sm|Math_Symbol|Sc|Currency_Symbol|Sk|Modifier_Symbol|So|Other_Symbol|Z|Separator|Zs|Space_Separator|Zl|Line_Separator|Zp|Paragraph_Separator|C|Other|Cc|Control|Cf|Format|Cs|Surrogate|Co|Private_Use|Cn|Unassigned|Alpha|Alphabetic|Cased|Emoji|Math|Lowercase|Uppercase|White_Space|Bidi_Control|Hex_Digit|ASCII_Hex_Digit|Noncharacter_Code_Point|Default_Ignorable_Code_Point|Regional_Indicator|Join_Control)(?:&\\[pP]\{(?:(?:Is|gc|General_Category)=)?(?:L|Letter|Lu|Uppercase_Letter|Ll|Lowercase_Letter|Lt|Titlecase_Letter|Lm|Modifier_Letter|Lo|Other_Letter|M|Mark|Mn|Nonspacing_Mark|Mc|Spacing_Mark|Me|Enclosing_Mark|N|Number|Nd|Decimal_Number|Nl|Letter_Number|No|Other_Number|P|Punctuation|Pc|Connector_Punctuation|Pd|Dash_Punctuation|Ps|Open_Punctuation|Pe|Close_Punctuation|Pi|Initial_Punctuation|Pf|Final_Punctuation|Po|Other_Punctuation|S|Symbol|Sm|Math_Symbol|Sc|Currency_Symbol|Sk|Modifier_Symbol|So|Other_Symbol|Z|Separator|Zs|Space_Separator|Zl|Line_Separator|Zp|Paragraph_Separator|C|Other|Cc|Control|Cf|Format|Cs|Surrogate|Co|Private_Use|Cn|Unassigned|Alpha|Alphabetic|Cased|Emoji|Math|Lowercase|Uppercase|White_Space|Bidi_Control|Hex_Digit|ASCII_Hex_Digit|Noncharacter_Code_Point|Default_Ignorable_Code_Point|Regional_Indicator|Join_Control)\})*\}

```

32.  **OAuth 2.0 Bearer Token Authentication Header**

```
(?i)(?:Authorization\s*:\s*Bearer\s+)(?:[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+|[a-zA-Z0-9\-_]{64,})

```

33.  **XML Namespace Declaration Parser**

```
xmlns(?::[a-zA-Z][a-zA-Z0-9-_]*)?="(?:http:\/\/[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\/[a-zA-Z0-9\-\._~:\/?#\[\]@!\$&'\(\)\*\+,;=]*|urn:[a-z0-9][a-z0-9-]{0,31}:[a-z0-9()+,\-.:=@;$_!*'%/?#]+)"

```

34.  **Protocol Buffer Field Definition**

```
(?:repeated|optional|required)?\s+(?:double|float|int32|int64|uint32|uint64|sint32|sint64|fixed32|fixed64|sfixed32|sfixed64|bool|string|bytes|(?:[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*))(?:\s+map<(?:[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*),\s*(?:[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)>)?\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([0-9]+)\s*(?:\[\s*(?:deprecated|default\s*=\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[a-zA-Z_][a-zA-Z0-9_]*|(?:-?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)|true|false))\s*\])?;

```

35.  **Django Template Language Parser**

```
\{%\s*(?:if|for|block|extends|include|load|with|autoescape|comment|csrf_token|cycle|debug|filter|firstof|lorem|now|regroup|resetcycle|spaceless|templatetag|url|verbatim|widthratio)\s+(?:[^{%]|\{[^%]|%[^}])*\s*(?:%\}(?:[^{%]|\{[^%]|%[^}])*\{%\s*end(?:if|for|block|autoescape|comment|filter|spaceless|verbatim)\s*%\})?|\}\})

```

36.  **Comprehensive Scientific Notation Number**

```
(?<![\w.])(?i)(?:[+-]?(?=\d*[.eE])(?=\.?\d)\d*\.?\d*(?:[eE][+-]?\d+)?|[+-]?0x[\dA-F]+(?:\.[\dA-F]*)?[Pp][+-]?\d+|[+-]?0x[\dA-F]+(?:\.[\dA-F]*)?|[+-]?[0-9]+(?:\.[0-9]*)?)(?![\w.])

```

37.  **Complex Kubernetes Resource Definition**

```
apiVersion:\s*[a-zA-Z0-9/.-]+\s+kind:\s*[a-zA-Z0-9]+\s+metadata:\s+(?:name:\s*[a-zA-Z0-9.-]+\s+)?(?:namespace:\s*[a-zA-Z0-9.-]+\s+)?(?:labels:\s+(?:[a-zA-Z0-9.-]+:\s*[a-zA-Z0-9.-]+\s+)*)?(?:annotations:\s+(?:[a-zA-Z0-9.-]+:\s*[^\n]+\s+)*)?spec:\s+(?:[^\{\}]|\{(?:[^\{\}]|\{(?:[^\{\}]|\{[^\{\}]*\})*\})*\})*

```

38.  **GraphQL Schema Definition**

```
(?:type|input|interface|enum|union|scalar|extend)\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:implements\s+(?:&\s*)?[A-Za-z_][A-Za-z0-9_]*(?:\s*&\s*[A-Za-z_][A-Za-z0-9_]*)*\s*)?(?:\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}|=\s*(?:[A-Za-z_][A-Za-z0-9_]*(?:\s*\|\s*[A-Za-z_][A-Za-z0-9_]*)*)\s*|;)

```

39.  **Advanced crontab Expression Parser**

```
(?:@(?:annually|yearly|monthly|weekly|daily|hourly|reboot)|(?:(?:(?:[0-5]?[0-9]|(?:[0-5]?[0-9])(?:-|,)(?:[0-5]?[0-9])|(?:[0-5]?[0-9])(?:-|,)(?:[0-5]?[0-9])(?:\/|,)(?:[0-5]?[0-9])|\*)(?:\s+(?:(?:[0-5]?[0-9]|(?:[0-5]?[0-9])(?:-|,)(?:[0-5]?[0-9])|(?:[0-5]?[0-9])(?:-|,)(?:[0-5]?[0-9])(?:\/|,)(?:[0-5]?[0-9])|\*)(?:\s+(?:(?:0?[1-9]|[12][0-9]|3[01]|(?:(?:0?[1-9]|[12][0-9]|3[01])(?:-|,)(?:0?[1-9]|[12][0-9]|3[01]))|(?:(?:0?[1-9]|[12][0-9]|3[01])(?:-|,)(?:0?[1-9]|[12][0-9]|3[01]))(?:\/|,)(?:0?[1-9]|[12][0-9]|3[01])|\*)(?:\s+(?:(?:(?:0?[1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|\*)|(?:(?:0?[1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(?:-|,)(?:0?[1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))|(?:(?:0?[1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(?:-|,)(?:0?[1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))(?:\/|,)(?:0?[1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)))(?:\s+(?:(?:(?:[0-7]|MON|TUE|WED|THU|FRI|SAT|SUN)|\*)|(?:(?:[0-7]|MON|TUE|WED|THU|FRI|SAT|SUN)(?:-|,)(?:[0-7]|MON|TUE|WED|THU|FRI|SAT|SUN))|(?:(?:[0-7]|MON|TUE|WED|THU|FRI|SAT|SUN)(?:-|,)(?:[0-7]|MON|TUE|WED|THU|FRI|SAT|SUN))(?:\/|,)(?:[0-7]|MON|TUE|WED|THU|FRI|SAT|SUN))))))))))\s+(?:(?:[^\s])+)(?:\s+(?:(?:[^\s])+))*

```

40.  **Complex Bitcoin Address Validator**

```
(?:[13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{11,71}|(?:0x)?[a-fA-F0-9]{40})

```

41.  **Docker Compose Network Configuration**

```
networks:\s+([a-zA-Z0-9._-]+):\s+(?:driver:\s+([a-zA-Z0-9._-]+)\s+)?(?:driver_opts:\s+(?:[a-zA-Z0-9._-]+:\s+[^\n]+\s+)*)?(?:ipam:\s+(?:driver:\s+([a-zA-Z0-9._-]+)\s+)?config:\s+(?:-\s+subnet:\s+(?:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})\s+(?:ip_range:\s+(?:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})\s+)?(?:gateway:\s+(?:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+)?)*)

```

42.  **FFmpeg Complex Filter Graph**

```
(?:[a-zA-Z0-9_]+)(?:\[[a-zA-Z0-9_:]+\])?(?:=(?:[a-zA-Z0-9_]+(?:=(?:[^:,[\]]+|\[[^\[\]]+\])+)?(?::[a-zA-Z0-9_]+(?:=(?:[^:,[\]]+|\[[^\[\]]+\])+)?)*))?,?(?:[a-zA-Z0-9_]+)(?:\[[a-zA-Z0-9_:]+\])?(?:=(?:[a-zA-Z0-9_]+(?:=(?:[^:,[\]]+|\[[^\[\]]+\])+)?(?::[a-zA-Z0-9_]+(?:=(?:[^:,[\]]+|\[[^\[\]]+\])+)?)*))?,?(?:[a-zA-Z0-9_]+)(?:\[[a-zA-Z0-9_:]+\])?(?:=(?:[a-zA-Z0-9_]+(?:=(?:[^:,[\]]+|\[[^\[\]]+\])+)?(?::[a-zA-Z0-9_]+(?:=(?:[^:,[\]]+|\[[^\[\]]+\])+)?)*))

```

43.  **PHP Docblock Annotation Parser**

```
(?:/\*\*(?:\s*\*[ \t]*@(?:param|return|throws|var|method|property|property-read|property-write)\s+(?:(?:[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*\\)*[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*(?:\[\])?(?:\|(?:(?:[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*\\)*[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*(?:\[\])?|\?(?:(?:[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*\\)*[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*))+)?\s+(?:\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*)?\s*(?:(e?:-|\*)\s*.+?)?)?\s*)*\*/)

```

44.  **AWS CloudFormation Resource Definition**

```
(?:"Type"\s*:\s*"(?:AWS::(?:ApiGateway|AppSync|ApplicationAutoScaling|Athena|AutoScaling|Batch|Budgets|CertificateManager|Cloud9|CloudFormation|CloudFront|CloudTrail|CloudWatch|CodeBuild|CodeCommit|CodeDeploy|CodePipeline|CodeStar|Cognito|Config|DataPipeline|DAX|DMS|DynamoDB|EC2|ECR|ECS|EFS|Elasticsearch|ElasticLoadBalancing|ElasticLoadBalancingV2|EMR|Events|GameLift|Glue|GuardDuty|IAM|Inspector|IoT|IoT1Click|KMS|Lambda|Logs|OpsWorks|RDS|Redshift|Route53|S3|SageMaker|SecretsManager|ServiceCatalog|ServiceDiscovery|SES|SNS|SQS|SSM|StepFunctions|WAF|WAFRegional|WorkSpaces)::[a-zA-Z0-9]+)")(?:(?:.|\s)*?)(?:"Properties"\s*:\s*\{(?:(?:[^{}]|\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\})*)\})

```

45.  **Kubernetes CronJob Resource Definition**

```
apiVersion:\s*batch/v1beta1\s+kind:\s*CronJob\s+metadata:\s+(?:name:\s*[a-zA-Z0-9.-]+\s+)?(?:namespace:\s*[a-zA-Z0-9.-]+\s+)?(?:labels:\s+(?:[a-zA-Z0-9.-]+:\s*[a-zA-Z0-9.-]+\s+)*)?(?:annotations:\s+(?:[a-zA-Z0-9.-]+:\s*[^\n]+\s+)*)?spec:\s+schedule:\s*"[^\n"]+"\s+(?:concurrencyPolicy:\s*(?:Allow|Forbid|Replace)\s+)?(?:failedJobsHistoryLimit:\s*[0-9]+\s+)?(?:startingDeadlineSeconds:\s*[0-9]+\s+)?(?:successfulJobsHistoryLimit:\s*[0-9]+\s+)?(?:suspend:\s*(?:true|false)\s+)?jobTemplate:\s+spec:\s+template:\s+spec:\s+(?:(?:volumes:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+(?:configMap|secret|hostPath|emptyDir|persistentVolumeClaim):\s+(?:[^\n]+\s+)+)+)?(?:initContainers:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+image:\s*[^\n]+\s+(?:command:\s+(?:-\s+[^\n]+\s+)+)?(?:args:\s+(?:-\s+[^\n]+\s+)+)?(?:env:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+value(?:From)?:\s+[^\n]+\s+)+)?(?:volumeMounts:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+mountPath:\s*[^\n]+\s+(?:readOnly:\s*(?:true|false)\s+)?)+)?)+)?containers:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+image:\s*[^\n]+\s+(?:command:\s+(?:-\s+[^\n]+\s+)+)?(?:args:\s+(?:-\s+[^\n]+\s+)+)?(?:env:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+value(?:From)?:\s+[^\n]+\s+)+)?(?:volumeMounts:\s+(?:-\s+name:\s*[a-zA-Z0-9.-]+\s+mountPath:\s*[^\n]+\s+(?:readOnly:\s*(?:true|false)\s+)?)+)?)+(?:restartPolicy:\s*(?:Always|OnFailure|Never)\s+)?)

```


46.  **Discover Card Validation (Full Implementation)**

```
65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})

```

47.  **Switch Card Validation**

```
(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{15}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{14}

```

48.  **Mastercard Validation (With New 2-Series)**

```
(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))

```

49.  **Full RFC 5322 Email (Without Comments, Canonical Form)**

```
([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|"([]!#-[^-~ \t]|(\\[\t -~]))+")@([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\[[\t -Z^-~]*)

```

50.  **Full RFC 5322 Email (With Folding Whitespace)**

```
((([\t ]*\r\n)?[\t ]+)?[-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*(([\t ]*\r\n)?[\t ]+)?|(([\t ]*\r\n)?[\t ]+)?"(((([\t ]*\r\n)?[\t ]+)?([]!#-[^-~]|(\\[\t -~])))+(([\t ]*\r\n)?[\t ]+)?|(([\t ]*\r\n)?[\t ]+)?)"(([\t ]*\r\n)?[\t ]+)?)@((([\t ]*\r\n)?[\t ]+)?[-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*(([\t ]*\r\n)?[\t ]+)?|(([\t ]*\r\n)?[\t ]+)?\[((([\t ]*\r\n)?[\t ]+)?[!-Z^-~])*(([\t ]*\r\n)?[\t ]+)?](([\t ]*\r\n)?[\t ]+)?)

```

51.  **Unicode URL Pattern (International Domain Support)**

```
((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)|(([a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+([a-z\u00a1-\uffff]{2,}\.?)

```

52.  **HTML Tag Parser (With Attribute Support)**

```
<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>|<(?:[a-zA-Z][a-zA-Z0-9-]*)((?:\s+[a-zA-Z0-9-]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^>\s]+))?)*)(?:\s*\/?)?>

```

53.  **Complete CSS Property with Vendor Prefixes**

```
(?:^|\s*)(?:\-(?:webkit|moz|ms|o)\-)?([a-z\-]+)\s*:\s*(?:(?:'(?:\\'|[^'])*?')|(?:"(?:\\"|[^"])*?")|([^;]+?))(?:\s*;|\s*$)

```

54.  **Complex XML Tag with Namespaces and Attributes**

```
<\s*([a-zA-Z_:][-a-zA-Z0-9_:.]*)((?:\s+[a-zA-Z_:][-a-zA-Z0-9_:.]*)(?:\s*=\s*(?:'[^']*?'|"[^"]*?"|[-a-zA-Z0-9_./:]+))?)*\s*(?:\/\s*)?|(?:\/\s*)?>

```

55.  **ISBN-13 with Formatting**

```
(?:ISBN(?:-13)?:?\s*)?(?=[0-9X]{13}$|(?=(?:[0-9]+[-\s]){3})[-\s0-9X]{17}$)97[89][-\s]?[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9X]$

```

56.  **Complete US Phone Number (All Formats)**

```
((?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]|[2-9]9[02-9])\s*\)|(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]|[2-9]9[02-9]))\s*(?:[.-]\s*)?)?(?:[2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?(?:[0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(?:[0-9]+))?

```

57.  **JSON Parser (Generic Value)**

```
("(?:[^"\\]|\\.)*")|(-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)|(\btrue\b|\bfalse\b|\bnull\b)|(\{(?:[^"{}]|"(?:[^"\\]|\\.)*"|\{(?:[^"{}]|"(?:[^"\\]|\\.)*")*\})*\})|(\[(?:[^"\[\]]|"(?:[^"\\]|\\.)*"|\[(?:[^"\[\]]|"(?:[^"\\]|\\.)*")*\])*\])

```

58.  **Password Strength with Requirements**

```
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~`!@#$%^&*()_\-+={}[\]\\|:;"'<>,.?\/])[A-Za-z\d~`!@#$%^&*()_\-+={}[\]\\|:;"'<>,.?\/]{12,}(?=(.*[a-z]){3,})(?=(.*[A-Z]){2,})(?=(.*\d){2,})(?=(.*[~`!@#$%^&*()_\-+={}[\]\\|:;"'<>,.?\/]){2,})([A-Za-z\d~`!@#$%^&*()_\-+={}[\]\\|:;"'<>,.?\/]){10,}

```

59.  **Nested XML Document Structure**

```
<([a-zA-Z][a-zA-Z0-9:]*-?[a-zA-Z0-9:]*)(?:\s+[a-zA-Z0-9:]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^<>\s]+))?)*\s*(?:>(.*?)</\1\s*>|\s*/>)

```

60.  **International Phone Number (ITU-T E.164)**

```
(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?

```

61.  **Hexadecimal Color with Alpha (All Formats)**

```
(?:#?(?:[0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})|rgba?\((?:\s*\d+\s*,){2}\s*\d+\s*(?:,\s*\d+(?:\.\d+)?\s*)?\)|hsla?\((?:\s*\d+\s*,){2}\s*\d+\s*(?:,\s*\d+(?:\.\d+)?\s*)?\))

```

62.  **CSS Media Query Parser**

```
@media\s+(?:only\s+)?(?:(?:[a-z-]+\s*,?\s*)+)(?:\s+and\s+)?(?:\(\s*[a-z-]+\s*(?::\s*[^()\n]+\s*)?\)(?:\s+and\s+\(\s*[a-z-]+\s*(?::\s*[^()\n]+\s*)?\))*)?

```

63.  **Complete Date Parser (All Common Formats)**

```
(?:(?:(?:(?:(?:[1-9]\d)(?:0[48]|[2468][048]|[13579][26])|(?:(?:[2468][048]|[13579][26])00))(?:\/|-|\.)(?:0?2)(?:\/|-|\.)(?:29))|(?:(?:[1-9]\d{3})(?:\/|-|\.)(?:(?:0?[13578]|1[02])(?:\/|-|\.)31)|(?:(?:0?[13-9]|1[0-2])(?:\/|-|\.)(?:29|30))|(?:(?:0?[1-9])|(?:1[0-2]))(?:\/|-|\.)(?:0?[1-9]|1\d|2[0-8]))))|(?:(?:[1-9]\d{3})([\-\/\.])(0?[1-9]|1[0-2])\2(0?[1-9]|1\d|2[0-8]))|(?:(?:(?:[1-9]\d)(?:0[48]|[2468][048]|[13579][26])|(?:(?:[2468][048]|[13579][26])00))([\-\/\.])(0?2)\4(29)))

```

64.  **Complex SQL Query Parser**

```
(SELECT\s+(?:(?:ALL|DISTINCT)\s+)?(?:(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+(?:\s+as\s+[a-zA-Z0-9_]+)?|\*|(?:\([^\(\)]+\))(?:\s+as\s+[a-zA-Z0-9_]+)?))(?:\s*,\s*(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+(?:\s+as\s+[a-zA-Z0-9_]+)?|\*|(?:\([^\(\)]+\))(?:\s+as\s+[a-zA-Z0-9_]+)?))*)?\s+FROM\s+(?:[a-zA-Z0-9_]+(?:\s+as\s+[a-zA-Z0-9_]+)?))(?:\s+(?:INNER|LEFT|RIGHT|OUTER|CROSS|NATURAL)?\s*JOIN\s+(?:[a-zA-Z0-9_]+(?:\s+as\s+[a-zA-Z0-9_]+)?)\s+(?:ON|USING)\s+(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+\s*=\s*(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+|\([^\(\)]+\)))*(?:\s+WHERE\s+[^\s;]+(?:\s+(?:AND|OR)\s+[^\s;]+)*)?(?:\s+GROUP\s+BY\s+(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+)(?:\s*,\s*(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+))*)?(?:\s+HAVING\s+(?:[^\s;]+)(?:\s+(?:AND|OR)\s+(?:[^\s;]+))*)?(?:\s+ORDER\s+BY\s+(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+|\d+)(?:\s+(?:ASC|DESC))?(?:\s*,\s*(?:(?:[a-zA-Z0-9_]+\.)?[a-zA-Z0-9_]+|\d+)(?:\s+(?:ASC|DESC))?)*)?)(?:\s+LIMIT\s+\d+(?:\s*,\s*\d+)?)?

```

65.  **LDAP Distinguished Name Parser**

```
(?:(?:CN|OU|DC|O|L|S|C|STREET|E|UID|MAIL)=(?:(?:[^,+="<>#;\\]|\\[,+="<>#;\\])+|"(?:[^"\\]|\\.)*"))(?:\+(?:(?:CN|OU|DC|O|L|S|C|STREET|E|UID|MAIL)=(?:(?:[^,+="<>#;\\]|\\[,+="<>#;\\])+|"(?:[^"\\]|\\.)*")))*(?:,(?:(?:CN|OU|DC|O|L|S|C|STREET|E|UID|MAIL)=(?:(?:[^,+="<>#;\\]|\\[,+="<>#;\\])+|"(?:[^"\\]|\\.)*"))(?:\+(?:(?:CN|OU|DC|O|L|S|C|STREET|E|UID|MAIL)=(?:(?:[^,+="<>#;\\]|\\[,+="<>#;\\])+|"(?:[^"\\]|\\.)*")))*)*

```

66.  **HTML Comment with Conditional IE Statements**

```
<!--(?:(?!<!--|-->)[\s\S])*(?:<!(?:--)?\[if\s+(?:[^\[\]]+|\[(?:[^\[\]]+|\[[^\[\]]*\])*\])*\](?:--)?>(?:(?!<!--|-->)[\s\S])*)?-->

```

67.  **JWT (JSON Web Token) Validation**

```
(?:([A-Za-z0-9-_]{4,}(?:\.[A-Za-z0-9-_]{4,}){2})|([A-Za-z0-9-_]{4,}\.(?:[A-Za-z0-9-_]{4,}\.[A-Za-z0-9-_]{4,}(?:\.[A-Za-z0-9-_]{4,})*)))

```

68.  **GraphQL Query Parser**

```
(?:query|mutation|subscription)\s+(?:[_A-Za-z][_0-9A-Za-z]*\s*)?(?:\(\s*(?:[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:\[\s*[_A-Za-z][_0-9A-Za-z]*(?:\s*\[\s*[_A-Za-z][_0-9A-Za-z]*\s*\])*\s*[!]?\s*\]|[_A-Za-z][_0-9A-Za-z]*(?:\s*\[\s*[_A-Za-z][_0-9A-Za-z]*\s*\])*)\s*[!]?\s*(?:,\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:\[\s*[_A-Za-z][_0-9A-Za-z]*(?:\s*\[\s*[_A-Za-z][_0-9A-Za-z]*\s*\])*\s*[!]?\s*\]|[_A-Za-z][_0-9A-Za-z]*(?:\s*\[\s*[_A-Za-z][_0-9A-Za-z]*\s*\])*)\s*[!]?\s*)*\s*\))?\s*\{\s*(?:[_A-Za-z][_0-9A-Za-z]*\s*(?:\(\s*(?:[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\[\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*(?:,\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*)*\s*\])|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\})))\s*(?:,\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\[\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*(?:,\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*)*\s*\])|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\})))\s*)*\s*\))?\s*\{\s*.*?\s*\}|[_A-Za-z][_0-9A-Za-z]*)\s*(?:,\s*(?:[_A-Za-z][_0-9A-Za-z]*\s*(?:\(\s*(?:[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\[\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*(?:,\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*)*\s*\])|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\})))\s*(?:,\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\[\s*(?:(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*(?:,\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null)|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\}))\s*)*\s*\])|(?:\{\s*[_A-Za-z][_0-9A-Za-z]*\s*:\s*(?:"(?:[^"]|\\")*"|(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?:true|false|null))\s*\})))\s*)*\s*\))?\s*\{\s*.*?\s*\}|[_A-Za-z][_0-9A-Za-z]*))\s*)*\s*\}

```

69.  **Advanced HTML Entity Decoder**

```
&(?:[a-zA-Z][a-zA-Z0-9]{1,31}|#[0-9]{1,7}|#[xX][0-9a-fA-F]{1,6});|&#(?:(?:[0-9]{1,7})|(?:[xX][0-9a-fA-F]{1,6}));

```

70.  **ETL Data Transformation Parser**

```
\s*(?:(?:(?:(?:CREATE|REPLACE)\s+)?VIEW\s+(?:IF\s+NOT\s+EXISTS\s+)?(?:[a-zA-Z0-9_]+\.)?\s*[a-zA-Z0-9_]+\s+(?:SECURITY\s+(?:DEFINER|INVOKER)\s+)?(?:SQL\s+SECURITY\s+(?:DEFINER|INVOKER)\s+)?AS\s+)?\s*(?:WITH\s+(?:[a-zA-Z0-9_]+\s+AS\s+\(\s*(?:SELECT|WITH|VALUES).+?\s*\)\s*(?:,\s*[a-zA-Z0-9_]+\s+AS\s+\(\s*(?:SELECT|WITH|VALUES).+?\s*\)\s*)*))?\s*(?:SELECT(?:\s+(?:ALL|DISTINCT))?\s+(?:.+?\s+FROM\s+(?:(?:[a-zA-Z0-9_]+\s+(?:(?:(?:LEFT|RIGHT|INNER|OUTER|FULL|CROSS)\s+)?JOIN\s+[a-zA-Z0-9_]+\s+(?:AS\s+)?[a-zA-Z0-9_]+\s+ON\s+.+?|,\s*[a-zA-Z0-9_]+(?:\s+(?:AS\s+)?[a-zA-Z0-9_]+)?))*)))|(?:INSERT(?:\s+INTO)?\s+(?:[a-zA-Z0-9_]+\.)?\s*[a-zA-Z0-9_]+\s+(?:\(\s*[a-zA-Z0-9_]+(?:\s*,\s*[a-zA-Z0-9_]+\s*)*\))?\s+(?:VALUES\s+\(\s*.+?\s*\)(?:\s*,\s*\(\s*.+?\s*\))*|SELECT\s+.+?)))\s*(?:(?:WHERE|GROUP\s+BY|HAVING|ORDER\s+BY|LIMIT|OFFSET|FETCH|FOR|UNION\s+(?:ALL)?)\s+.+?)?\s*;?

```

71.  **MongoDB Query Parser**

```
\{\s*(?:(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\[\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\}|\[\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\])\s*(?:,\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\}|\[\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\])\s*)*\]|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\}|\[\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\])\s*(?:,\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\}|\[\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\])\s*)*\})\s*\})\s*(?:,\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null|\{\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')\s*:\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\}|\[\s*(?:"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null)\s*\])\s*)*\s*\}

```

72.  **Comprehensive JavaScript String Literals Parser**

```
(?:'(?:[^'\\]|\\['\\bfnrt]|\\u[0-9a-fA-F]{4}|\\x[0-9a-fA-F]{2}|\\[^'\\bfnrtv0-9xu])*'|"(?:[^"\\]|\\["\\bfnrt]|\\u[0-9a-fA-F]{4}|\\x[0-9a-fA-F]{2}|\\[^"\\bfnrtv0-9xu])*"|`(?:[^`\\]|\\[`\\bfnrt]|\\u[0-9a-fA-F]{4}|\\x[0-9a-fA-F]{2}|\\[^`\\bfnrtv0-9xu]|\$\{(?:[^{}]|\{[^{}]*\})*\})*`)

```

73.  **Log File Analyzer with Timestamps and Levels**

```
(?<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:[+-]\d{2}:\d{2}|Z)?)(?:\s+(?<hostname>(?:(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*(?:[A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])))?(?:\s+(?<application>[^\s\[\]:]+))?(?:\s+\[(?<pid>\d+)\])?(?:\s+(?<level>TRACE|DEBUG|INFO|NOTICE|WARN|WARNING|ERROR|CRITICAL|ALERT|EMERGENCY|[A-Z]+))?(?:\s+(?<thread>\[(?:[^\[\]]+|\[[^\[\]]*\])*\]))?(?:\s+)?(?<message>.*)

```

74.  **CMS Template Parser with Variables and Filters**

```
\{\{\s*(?:(?<variable>[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*(?:\[[^\[\]]+\])*)(?:\s*\|\s*(?<filter>[a-zA-Z0-9_]+)(?:\s*:\s*(?<filter_arg>(?:[^|}]+|(?:\{[^{}]*\})|(?:\([^()]*\)))))?)*|(?<tag>if|for|while|unless|with)\s+(?<condition>[^{}]+))\s*\}\}(?<content>.*?)(?:\{\{\s*(?<endtag>end(?:if|for|while|unless|with))\s*\}\})?

```

75.  **Semantic Versioning with Build and Pre-release Metadata**

```
(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?

```


76.  **Matching valid email addresses ending with @example.com**

```
(?:(?:[a-zA-Z0-9]|(?:[a-zA-Z0-9][-_\.]{0,1}[a-zA-Z0-9]))+)(?:(?:(?:(?:(?:@){1})(?:(?:(?:[eE]){1})(?:(?:[xX]){1})(?:(?:[aA]){1})(?:(?:[mM]){1})(?:(?:[pP]){1})(?:(?:[lL]){1})(?:(?:[eE]){1})(?:(?:[\.]{1})(?:(?:[cC]){1})(?:(?:[oO]){1})(?:(?:[mM]){1}))))(?![a-zA-Z0-9]))

```

77. **Representing allowed requests within an access control policy**

```
arn:aws:s3:::xxx/(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((\?|/)|7)|')|;)|\+)|3)|\#)|=)|-)|5)|%)|9)|\))|1)|!)|>)|\.)|6)|\&)|:)|\*)|2)|\")|<)|,)|4)|$)|8)|\()|0)| )|_)|O)|W)|G)|\[)|K)|S)|C)|\])|M)|U)|E)|Y)|I)|Q)|A)|^)|N)|V)|F)|Z)|J)|R)|B)|\\)|L)|T)|D)|X)|H)|P)|\@)|o)|g)|k)|c)|m)|e)|i)|a)|n)|f)|j)|b)|l)|d)|h)|`)|w)|s)|u)|q)|v)|r)|t)|p)|\{)|y)|z)|x)|\})|\|)|\~))*

```
78. **Representing allowed requests within an access control policy**

```
(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((\?|/)|7)|')|;)|\+)|3)|\#)|=)|-)|5)|%)|9)|\))|1)|!)|>)|\.)|6)|\&)|:)|\*)|2)|\"")|<)|,)|4)|$)|8)|\()|0)| )|_)|O)|W)|G)|\[)|K)|S)|C)|\])|M)|U)|E)|Y)|I)|Q)|A)|^)|N)|V)|F)|Z)|J)|R)|B)|\\)|L)|T)|D)|X)|H)|P)|\@)|o)|g)|k)|c)|m)|e)|i)|a)|n)|f)|j)|b)|l)|d)|h)|`)|w)|s)|u)|q)|v)|r)|t)|p)|\{)|y)|z)|x)|\})|\|)|\~))*

```

79. **Representing allowed requests within an access control policy**

```
arn:aws:ec2:us-east-1:(:image/ami-|1234123412(43:instance/|34:((key-pair|s(ubnet|ecurity-group))/|(volum|network-interfac)e/)))(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((\?|/)|7)|')|;)|\+)|3)|\#)|=)|-)|5)|%)|9)|\))|1)|!)|>)|\.)|6)|\&)|:)|\*)|2)|\")|<)|,)|4)|$)|8)|\()|0)| )|_)|O)|W)|G)|\[)|K)|S)|C)|\])|M)|U)|E)|Y)|I)|Q)|A)|^)|N)|V)|F)|Z)|J)|R)|B)|\\)|L)|T)|D)|X)|H)|P)|\@)|o)|g)|k)|c)|m)|e)|i)|a)|n)|f)|j)|b)|l)|d)|h)|`)|w)|s)|u)|q)|v)|r)|t)|p)|\{)|y)|z)|x)|\})|\|)|\~))*

```

80. **Representing allowed requests within an access control policy**

```
arn:aws:s3:::billing(|/(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((\?|/)|7)|')|;)|\+)|3)|\#)|=)|-)|5)|%)|9)|\))|1)|!)|>)|\.)|6)|\&)|:)|\*)|2)|\")|<)|,)|4)|$)|8)|\()|0)| )|_)|O)|W)|G)|\[)|K)|S)|C)|\])|M)|U)|E)|Y)|I)|Q)|A)|^)|N)|V)|F)|Z)|J)|R)|B)|\\)|L)|T)|D)|X)|H)|P)|\@)|o)|g)|k)|c)|m)|e)|i)|a)|n)|f)|j)|b)|l)|d)|h)|`)|w)|s)|u)|q)|v)|r)|t)|p)|\{)|y)|z)|x)|\})|\|)|\~))*)

```

81. **Representing allowed requests within an access control policy**

```
arn:aws:s3:::example/(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((\?|/)|7)|')|;)|\+)|3)|\#)|=)|-)|5)|%)|9)|\))|1)|!)|>)|\.)|6)|\&)|:)|\*)|2)|\")|<)|,)|4)|$)|8)|\()|0)| )|_)|O)|W)|G)|\[)|K)|S)|C)|\])|M)|U)|E)|Y)|I)|Q)|A)|^)|N)|V)|F)|Z)|J)|R)|B)|\\)|L)|T)|D)|X)|H)|P)|\@)|o)|g)|k)|c)|m)|e)|i)|a)|n)|f)|j)|b)|l)|d)|h)|`)|w)|s)|u)|q)|v)|r)|t)|p)|\{)|y)|z)|x)|\})|\|)|\~))*

```
82. **Language of strings over {a, b} that contain an even number of 'a's AND an even number of 'b's.**

```
((aa)*(bb)*)* | ((aa)*(bb)*)*(ab(aa)*(bb)*ba(aa)*(bb)*)*

```
83. **Strings that start with user_ followed by zero or more characters from a specific allowed set, which includes alphanumeric characters, underscores, hyphens, dots, and a selection of punctuation marks.**

```
user_([a-zA-Z0-9._\-+=%*!~]|\?|\/|'|;|\#|=|\$|\(|\)|\&|:|\||\{|\}|\[|\]|<|>|,|\ )*

```
