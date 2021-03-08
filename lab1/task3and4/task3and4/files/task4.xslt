<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
          <head>
            <meta charset="utf-8"/>
          </head>
        <body>
            <table border="1">
                <caption>Items</caption>
                <tr>
                    <th>Price</th>
                    <th>Description</th>
                    <th>Image</th>
                </tr>
                <xsl:for-each select="items/item">
                <tr>
                    <td><xsl:value-of select="price" /></td>
                    <td><xsl:value-of select="description" /></td>
                    <td>
                      <xsl:element name="img">
                        <xsl:attribute name="src">
                          <xsl:value-of select="image_url"/>
                        </xsl:attribute>
                      </xsl:element>
                    </td>
                </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>