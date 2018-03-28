# -*-coding:utf-8-*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", "w", encoding="utf-8")

        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<thead>")
        fout.write("<tr>")
        fout.write("<th>地址</th>")
        fout.write("<th>名称</th>")
        fout.write("<th>价格</th>")
        fout.write("</tr>")
        fout.write("</thead>")


        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['price'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
