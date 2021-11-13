import os
from re import search
from django.http import response
from rest_framework import status, views
from rest_framework.response import Response
from consultasApp.models.querySearch import QuerySearch
from consultasApp.serializers.querySerializer import QuerySerializer
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime


class QueryDocumentView(views.APIView):
    def get(self, request, pk):
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        responsePDF = response.HttpResponse(content_type='application/pdf')
        responsePDF['Content-Disposition'] = 'attachment; filename="consulta.pdf"'
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        querySearch = QuerySearch.objects.get(search=pk)
        print(querySearch)
        # header
        pdf.setLineWidth(.3)
        pdf.setFont('Vera', 30)
        pdf.drawString(30, 750, 'Tu Buscador Latino')
        pdf.setFont('Vera', 16)
        pdf.drawString(410, 750, 'Fecha: ' +
                       datetime.now().strftime("%d/%m/%Y"))
        pdf.setFont('Vera', 21)
        pdf.drawString(50, 600, 'Reporte de la palabra ' + '" ' + querySearch.search +
                       ' " :')
        pdf.setFont('Vera', 20)
        pdf.drawString(50, 500, 'Cantidad de veces buscada: ' +
                       str(querySearch.amount))
        pdf.drawString(50, 470, 'Primera busqueda: ' + datetime.utcfromtimestamp(querySearch.firstSearch).strftime('%Y-%m-%d %H:%M:%S')
                       )
        pdf.drawString(50, 440, 'Última busqueda: ' + datetime.utcfromtimestamp(querySearch.lastSearch).strftime('%Y-%m-%d %H:%M:%S')
                       )
        pdf.drawString(50, 410, 'Número de resultados: ' +
                       str(querySearch.numberResults))

        pdf.save()
        pdfReturn = buffer.getvalue()
        buffer.close()
        responsePDF.write(pdfReturn)
        return responsePDF

    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
