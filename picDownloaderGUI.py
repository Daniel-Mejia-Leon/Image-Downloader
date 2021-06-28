from tkinter import *
import requests
from bs4 import BeautifulSoup
from requests.exceptions import InvalidSchema
from termcolor import colored
import os
from time import sleep

def close():
    screen.destroy()


def image_downloader(url, folder):
    os.mkdir(os.path.join(os.getcwd(), folder))
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    print(f'Images found {len(images)}')
    sleep(2)
    pic_number = 1
    no_processed_images = 0
    links = []

    for image in images:
        print('\n')
        print(f'Processing img {pic_number}, code: {image}')
        try:
            name = image['alt']
        except KeyError:
            print(f'alt not found for image {pic_number}')
            name = f'Alt_tag_not_found_for_{pic_number}'
        if name == '':
            name = f'Name_not_found_for_{pic_number}'
        try:

            # image_link = f'https://www.nationalgeographic.com.es{image["src"]}'
            # image_link = image["src"]
            if str(image_link) in links:
                print(colored(f'Image {pic_number} is png or jpg but is already saved', 'green'))
                pic_number +=1
                no_processed_images += 1
                continue
            if 'gif' in str(image_link) or 'GIF' in str(image_link):
                if 'data-src' in str(image):
                    # image_link = f'https://www.nationalgeographic.com.es{image["data-src"]}'
                    # image_link = ["data-src"]
                    pass
                if 'png' in str(image_link) or 'jpg' in str(image_link) or 'PNG' in str(image_link) or 'JPG' in str(image_link):
                    pass
                else:
                    print(colored(f'Image {pic_number} is not png or jpg. See image link belowbelow:\n{image_link}', 'red'))
                    no_processed_images += 1
                    pic_number += 1
                    continue
            if 'png' in str(image_link) or 'jpg' in str(image_link) or 'PNG' in str(image_link) or 'JPG' in str(image_link):
                print(colored(f'Image {pic_number} is png or jpg see image link below:\n{image_link}', 'green'))
                if 'jpg' in image_link or 'JPG' in image_link:
                    if 'jpg' in image_link:
                        image_link_dot_format = image_link.split('.jpg')[0] + '.jpg'
                        with open(name.replace(' ', '-').replace('/', '').replace('|', '-') + '.jpg', 'wb') as f:
                            im = requests.get(image_link_dot_format)
                            f.write(im.content)
                            print(f'Saved: {name}, {image_link_dot_format}')
                            pic_number += 1
                            links.append(str(image_link))
                            continue
                    if 'JPG' in image_link:
                        image_link_dot_format = image_link.split('.JPG')[0] + '.JPG'
                        with open(name.replace(' ', '-').replace('/', '').replace('|', '-') + '.JPG', 'wb') as f:
                            im = requests.get(image_link_dot_format)
                            f.write(im.content)
                            print(f'Saved: {name}, {image_link_dot_format}')
                            pic_number += 1
                            links.append(str(image_link))
                            continue

                if 'png' in image_link or 'PNG' in image_link:
                    if 'png' in image_link:
                        image_link_jpg = image_link.split('.png')[0] + '.png'
                        with open(name.replace(' ', '-').replace('/', '').replace('|', '-') + '.png', 'wb') as f:
                            im = requests.get(image_link_jpg)
                            f.write(im.content)
                            print(f'Saved: {name}, {image_link_jpg}')
                            pic_number += 1
                            links.append(str(image_link))
                            continue
                    if 'PNG' in image_link:
                        image_link_jpg = image_link.split('.PNG')[0] + '.PNG'
                        with open(name.replace(' ', '-').replace('/', '').replace('|', '-') + '.PNG', 'wb') as f:
                            im = requests.get(image_link_jpg)
                            f.write(im.content)
                            print(f'Saved: {name}, {image_link_jpg}')
                            pic_number += 1
                            links.append(str(image_link))
                            continue

            else:
                print(colored(f'Image {pic_number} is other image format. See Image link below:\n{image_link}', 'red'))
                pic_number += 1
                no_processed_images += 1
                continue

        except (InvalidSchema, OSError, KeyError):
            print('Initial error')
            # if InvalidSchema:
            #     print(f'InvalidSchema at image {pic_number}')
            # else:
            #     pass
            pic_number += 1
            continue

    print(f'Total images found {pic_number -1}\nTotal images processed {(pic_number - 1) - no_processed_images}')


    sleep(2)
    done = Label(screen, text=f'Analysis Done\nTotal Images found: {pic_number - 1}\nTotal Images processed: {(pic_number - 1) - no_processed_images}\n\n', font=('Arial', 17), fg='green')
    done.pack()
    advise = Label(screen, text=f'This might not be accurate, gif pictures wont be processed\n', font=('Roboto', 10), fg='red')
    advise.pack()
    # sleep(20)
    # screen.destroy()

screen = Tk()
screen.title('Image Downloader by Kid')

title = Label(screen, text='IMAGE DOWNLOADER', font=('Arial', 30))
title.pack()

space = Label(screen, text='')
space.pack()

instructions = Label(screen, text='Please enter the full url for the webpage you want to get the pictures downloaded'
                                  ' from.\nThe code might not be able to download pictures from websites whose security'
                                  ' level is high.\nAnd this is made to download .png and .jpg image formats only.\n'
                                  'The program will generate a new folder where the images will be stored in same directory'
                                  ' as the .exe/program location\nTo do another analysis press Close to Restart\n',
                     font=('Roboto', 10))
instructions.pack()
instructions1= Label(screen, text='The program might go on "not responding" status while processing information'
                                  '\nWait while processing or check the console for full details of whats going on.'
                                  , font=('Roboto', 10), fg='red')
instructions1.pack()

space = Label(screen, text='')
space.pack()

url = Label(screen, text='URL/LINK here.\ne.g. =>> https://www.guatemala.com', font=('Roboto', 15))
url.pack()

enter_url = Entry(screen, width=90, borderwidth=5, justify='center', font=('Roboto', 10))
enter_url.pack()

space = Label(screen, text='')
space.pack()

folder_name = Label(screen, text='Enter Folder Name', font=('Roboto', 15))
folder_name.pack()

folder_name_text = Entry(screen, width=50, borderwidth=5, justify='center', font=('Roboto', 12))
folder_name_text.pack()

space = Label(screen, text='')
space.pack()

enter = Button(screen, text=" START ", command=lambda: image_downloader(enter_url.get(), folder_name_text.get()), font=('Arial', 15))
enter.pack()

space = Label(screen, text='')
space.pack()

restart = Button(screen, text=" CLOSE TO RESTART ", command=lambda: close, font=('Arial', 12), fg='red')
restart.pack()

space = Label(screen, text='')
space.pack()

src = Label(screen, text='Source code at https://github.com/Daniel-Mejia-Leon', font=('Roboto', 10))
src.pack()

space = Label(screen, text='')
space.pack()


screen.mainloop()
