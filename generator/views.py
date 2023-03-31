from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from fpdf import FPDF
import mysql.connector
import json
import os
import math
from fpdf import XPos, YPos
import mimetypes
from django.http.response import HttpResponse
from time import sleep
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse
from django.template.loader import render_to_string
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


# Create your views here.

def home(request):
    context = {
        
        }
    return render(request, 'index.html', context)





def enter_code(request):
    error = ''
    if request.method == 'POST':
        form = ActivateCodeForm(request.POST)
        try:
            if form.is_valid():
                t = Code.objects.get(code=form.cleaned_data['code'])
                t.quantity += 1
                t.active = True
                t.save()
                return HttpResponseRedirect(reverse('generate'))
            #render(request, 'generate-image.html', context)
            #HttpResponseRedirect(reverse('generate'))
        except:
                error = 'Code introuvable!'

    else:
        form = ActivateCodeForm()

    context = {
        'form': form,
        'error': error,
        }
    return render(request, 'enter-code.html', context)






def generate(request):
    error = ''
    if request.method == 'POST':
        form = ActivateCodeForm(request.POST)
        try:
            if form.is_valid():
                    t = Code.objects.get(code=form.cleaned_data['code'])
                    t.quantity += 1
                    t.active = True
                    t.save()
                    code_r = request.POST.get('code')
                    if code_r != None:
                        context = {
                            'code': code_r,
                            }
                        return render(request, 'generate-image.html', context)
                    else:
                        error = ''
                        if request.method == 'POST':
                            form = ActivateCodeForm(request.POST)
                            try:
                                if form.is_valid():
                                    t = Code.objects.get(code=form.cleaned_data['code'])
                                    t.quantity += 1
                                    t.active = True
                                    t.save()
                                    return render(request, 'generate-image.html', context)
                                #HttpResponseRedirect(reverse('generate'))
                            except:
                                    error = 'Code introuvable!'

                        else:
                            form = ActivateCodeForm()

                        context = {
                            'form': form,
                            'error': error,
                            }
                        return render(request, 'enter-code.html', context)
        except:
                error = 'Code introuvable!'

    else:
        form = ActivateCodeForm()


    context = {
        'form': form,
        'error': error,
        }
    return render(request, 'enter-code.html', context)



@csrf_exempt
def save_pdf(request):
    
    path = "generator/static/generator/fonts/BebasNeuePro-Regular.ttf"
    path_b = "generator/static/generator/fonts/BebasNeuePro-Bold.ttf"
    art_path = 'generator/static/generator/art/'
    img_path = 'generator/static/generator/images/'
    json_path = 'generator/static/generator/json/'
        #1                                                                                                            #31                                                                                                                  #60
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
         #1                                                                                                                                                                                                                                                           #60
    c = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
        #1                                                                                                                                                                                                                                                                                                    #60
    a = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]
        #1
    b = [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 
        227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239]
                                                                    #60

    if request.method == 'POST':
        result_json = json.loads(request.POST.get('json')) # type dict
        result_svg = request.POST.get('svg') # type str
        date = request.POST.get('date') # str
        
        with open(art_path + f"art_{date}.svg", 'w') as f:
            f.write(result_svg)
            drawing = svg2rlg(art_path + f"art_{date}.svg")
            renderPM.drawToFile(drawing, art_path + f"art_{date}.png", fmt="PNG")

    
    with open(json_path + f"json.ison", 'w', encoding='utf-8') as f:
            json.dump(result_json, f)


    steps = result_json['sequence']
    fin = []
    for i in steps:
        if 0 <= i <= 59:
            fin.append('D'+str(d.index(i)+1))
        elif 60 <= i <= 119:
            fin.append('C'+str(c.index(i)+1))
        elif 120 <= i <= 179:
            fin.append('A'+str(a.index(i)+1))
        elif 180 <= i <= 239:
            fin.append('B'+str(b.index(i)+1))

    def func_chunks_num(lst, c_num):
        n = math.ceil(len(lst) / c_num)

        for x in range(0, len(lst), n):
            e_c = lst[x : n + x]

            if len(e_c) < n:
                e_c = e_c + [None for y in range(n - len(e_c))]
            yield e_c

    data = list(func_chunks_num(fin, c_num=309))
    filtered_list = list(filter(lambda ele:ele is not None, data[-1]))
    data[-1] = filtered_list

    class CustomPDF(FPDF):
    
        def header(self):
            # Устанавливаем лого
            self.image(img_path + 'logo_small.png', 10, 8, 35, 15, link='https://relaxity-art.fr')
            self.add_font('BebasNeuePro-Regular', '', path)
            self.set_font('BebasNeuePro-Regular', '', size=15)
    
            self.cell(90)
            self.image(img_path + 'sectors2.jpg', 140, 7, w=60, h=15)
    
            # Разрыв линии
            self.ln(32) # отступ между лого на каждой картинке и текстом 15
        
        def footer(self):
            self.set_y(-13)
            self.set_font('BebasNeuePro-Regular', '', size=16)
            # Добавляем номер страницы
            page = str(self.page_no())
            self.cell(0, 10, page, 0, 0, 'C')


    pdf = CustomPDF()
    pdf.add_page() # 1
    pdf.image(img_path + 'b2.png', x = 0, y = 0, w = 210, h = 297, type = '', link = '')
    pdf.image(art_path + f"art_{date}.png", 25, 70, w=160, h=160)
    pdf.ln(5)
    pdf.image(img_path + 'hash_relaxity.png', 10, 265, w=60, h=22, link='https://relaxity-art.fr')
    pdf.image(img_path + 'relaxity_site.png', 167, 280, w=35, h=7, link='https://relaxity-art.fr')
    pdf.image(img_path + 'sectors.jpg', 91, 250, w=30, h=30)

    g = pdf.image(img_path + 'sectors.jpg', 91, 250, w=30, h=30)
    pdf.add_font('BebasNeuePro-Bold', '', path_b)


    # Задаем параметры
    # ячейки - сектора
    width_cell_sec = 16 # ширина ячейки 16
    height_cell_sec = 6 # высота ячейки 16
    # ячейки - шаги
    width_cell_steps = 16
    height_cell_steps = 15 #28 10
    # прямоугольник
    width_rect = 190 # длина прямоугольника
    height_rect = 12 # высота прямоугольника
    x_rect = 11 # отступ прямоугольника слева


    count, t = 1, 0
    y_rect = 60 # отступ прямоугольника сверху 50
    offset = 40
    for row in data:
            if data.index(row) % 2 == 0 and  data.index(row) in range(0, 310, 12):
                # нечетная строка
                # рисуем прямоугольник
                pdf.add_page()
                y_rect = 60
                offset = 0
                pdf.set_draw_color(238, 238, 238)
                pdf.set_fill_color(238, 238, 238)
                pdf.rect(x=x_rect, y=y_rect+offset, w=width_rect, h=height_rect, style='DF', round_corners=True)
                offset+=40
            elif data.index(row) % 2 != 0 and data.index(row) in range(0, 310, 12):
                # нечетная строка
                # рисуем прямоугольник
                pdf.set_draw_color(238, 238, 238)
                pdf.set_fill_color(238, 238, 238)
                pdf.rect(x=x_rect, y=y_rect, w=width_rect, h=height_rect, style='DF', round_corners=True)

            elif data.index(row) % 2 != 0 and data.index(row) not in range(0, 310, 12):
                # любой список кроме 0, 12, ... и 
                # рисуем прямоугольник
                pdf.set_draw_color(238, 238, 238)
                pdf.set_fill_color(238, 238, 238)
                pdf.rect(x=x_rect, y=y_rect+offset, w=width_rect, h=height_rect, style='DF', round_corners=True) # 92, 132
                offset+=40 # отступ между блоками прямоугольника 80
            
            if data.index(row) == 308:
                y_rect = 210
                offset = 0
                width_rect = 200 # длина прямоугольника
                height_rect = 30 # высота прямоугольника
                pdf.set_draw_color(255, 255, 255)
                pdf.set_fill_color(255, 255, 255)
                pdf.rect(x=x_rect, y=y_rect+offset, w=width_rect, h=height_rect, style='F')


            for item in row:
                t=0
                pdf.set_font('BebasNeuePro-Bold', '', size=18)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(width_cell_sec, height_cell_sec, item, border=0, align="C", new_x=XPos.LEFT, new_y=YPos.LAST) # LAST
                    
                pdf.set_font('BebasNeuePro-Bold', '', size=10)
                pdf.set_text_color(119, 119, 119)
                pdf.cell(width_cell_steps, height_cell_steps, str(count+t), border=0, align="C")
                count+=1
            t += 12
            pdf.ln(20) # общий (одинаковый) отступ между всеми строками, 20 это 144 на листе


    context = {
        'date': date
        }
    


    pdf.output(f'generator/static/generator/pdfs/Instruction{date}.pdf')

    # Если [Errno 13] Permission denied:, то закрыть открытый файл в программе или попробовать удалить его
    sleep(3)

    return render(request, 'generate-image.html', context)





def download_pdf(request):
    date = request.GET.get('json_data')
    return JsonResponse({'url': f'http://127.0.0.1:8000/static/generator/pdfs/Instruction{date}.pdf'})









def success(request):


    context = {

    }
    return render(request, 'success.html', context)