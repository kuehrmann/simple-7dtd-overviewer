import os.path
import datetime

zoom_levels = 5

def write_overview_html(level, out_filename, max_xy):
    f = open(out_filename, "w")
    f.write("<html>\n")
    f.write("<head>")
    f.write("    <title>Simple 7DTD Overviewer</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    write_zoom_links(f)
    f.write("    <table border=\"0\" cellspacing=\"0\" cellpadding=\"0\">\n")
    for y in range(max_xy, -max_xy, -1):
        f.write("        <tr>\n")
        for x in range(-max_xy, max_xy, 1):
            f.write("            <td>")
            filename = "%d/%d/%d.png" % (level,x,y)
            if os.path.isfile(filename):
                f.write("<img src=\"" + filename + "\">")
            f.write("</td>\n")
        f.write("        </tr>\n")
    f.write("    </table>\n")
    f.write("<div>Generated on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + " </div>")
    f.write("</body>\n")
    f.close()

def write_zoom_links(out_file):
    out_file.write("Zoom: ")
    out_file.write("<a href=\"index.html\">0</a> ")
    for i in range(1, zoom_levels):
        out_file.write("<a href=\"index%d.html\">%d</a> " % (i,i))
    out_file.write("\n")

for i in range(zoom_levels):
    filename = "index.html"
    if i != 0:
        filename = "index%d.html" % (i)
    write_overview_html(i, filename , (i+1)*4)
