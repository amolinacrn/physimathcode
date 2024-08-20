export function convertirHTMLtoPDF(divpdfconverter) {
    const elementpdf = document.getElementById(divpdfconverter)
    html2pdf().from(elementpdf).save()
}
