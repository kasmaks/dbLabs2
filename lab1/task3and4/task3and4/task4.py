from lxml import etree

xslt_root = etree.XML('''\
    <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
            <html>
            <body>
                <table border="1">
                    <caption>
                    Items
                    </caption>
                    <tr>
                        <th>Price</th>
                        <th>Description</th>
                        <th>Item image</th>
                    </tr>
                    <xsl:for-each select="items/item">
                    <tr>
                        <td><xsl:value-of select="price" /></td>
                        <td><xsl:value-of select="description" /></td>
                        <td><xsl:value-of select="image_url" /></td>
                    </tr>
                    </xsl:for-each>
                </table>        
            </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>
''')

transform = etree.XSLT(xslt_root)
doc = etree.parse("./files/task3.xml")
result = transform(doc)

result.write("./files/task4.xslt", pretty_print=True, encoding="UTF-8")
