"""
Platform: CodeSignal

You are planning to add more supported extensions for some scripts,
so now you would also like to store information about the extensions which
each script supports. As a starting point, you'd like to obtain the (extension, script)
pairs from the dictionary, sorted lexicographically by the extensions
"""


def transposeDictionary(scriptByExtension):
    return sorted([[j, i] for i, j in scriptByExtension.items()])


print(
    transposeDictionary(
        {"validate": "py", "getLimits": "md", "generateOutputs": "json"}
    )
)
