from pyscript import display, document

def grades(e):
    document.getElementById('output1').innerHTML=" "
    fname = document.getElementById('text1').value
    lname = document.getElementById('text2').value
    Grade1 = int(document.getElementById('text3').value)
    Grade2 = int(document.getElementById('text4').value)
    Grade3 = int(document.getElementById('text5').value)
    Grade4 = int(document.getElementById('text6').value)
    Grade5 = int(document.getElementById('text7').value)
    Grade6 = int(document.getElementById('text8').value)

    units = (5, 1, 2, 5, 3, 5)
    Math, Pe, Ict, Science, Ss, Eng = units

    Add = (Grade1 * Math) + (Grade2 * Pe) + (Grade3 * Ict) + (Grade4 * Science) + (Grade5 * Ss) + (Grade6 * Eng)
    GWA = Add / (Math + Pe + Ict + Science + Ss + Eng)

    display(f'Hello there {fname} {lname}, your GWA is {GWA}', target="output1")