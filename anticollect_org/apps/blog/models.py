from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils.safestring import  mark_safe


#take name from path
def ImgName(img):
    arr = img.split('/')
    return arr[-1]

#image compression method
def compress(image):

    im = Image.open(image)
    # imR = im.resize(1600)
    # im_io = BytesIO()
    NewImageName = ImgName(image.name)
    # im_io.name = NewImageName
    im.save(NewImageName, 'JPEG', quality=60, )
    new_image = File(NewImageName, name=NewImageName)
    print('newImage', NewImageName)
    return new_image

def dublicateDelite(image):
    arr = image.split('/')
    arr2 = []
    for a in arr:
        if (arr2.count(a) == 0):
            arr2.append(a)
    newUrls = '/'.join(arr2)
    return newUrls

def newPath(imgPath, image):
    containPath = image.find(imgPath)
    if (containPath >0):
        return dublicateDelite(image)
    else:
        return imgPath + image

# def bannerImg(obj, image):
#     # imgPath = 'photo/' + str(obj.slug) + '/banner.jpeg'
#     # nPath = dublicateDelite(image)
#     return 'photo/' + str(obj.slug) + '/banner.jpeg'

def bannerImg(obj, image):
    imgPath = 'photo/' + str(obj.slug) + '/'
    # dublicateDelite(image)
    return newPath(imgPath, image)

class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    blockName = models.CharField('Краткий Заголовок', max_length=60, help_text='Завликающий краткий заголовок')
    LongBlockName = models.CharField('Полный Заголовок статьи', max_length=150, blank=True, null=True, help_text='Полный заголовок описывающий всю суть')
    slug = models.SlugField('название для url', blank=True, null=True, help_text='название для ссылки, должно быть из латинских букв и цифр')
    created = models.DateTimeField(auto_now_add=True)
    lastmod = models.DateTimeField(auto_now=True)
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1, blank=True, null=True)
    banner = models.ImageField('Баннер для статьи', upload_to=bannerImg, blank=True, null=True, max_length=500,
                               help_text='Добавить привлекательную картинку для статьи')
    text = HTMLField('Наполнение блока', blank=True, max_length=20000)
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='draft')
    metaDescrioption = models.CharField('Мета описание', max_length=155, null=True, blank=True,
                                        help_text='Описание страницы для поисковиков\n будет видно в снипете(выдача поиска в Google)')
    metaKeyWords = models.CharField('Ключевые слова', max_length=155, null=True, blank=True,
                                    help_text='ключевые слова с поисковиков по теме')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" />' % (self.banner))
    image_tag.short_description = 'Баннер'

    def get_absolute_url(self):
        return reverse('blog:BlogDetail', kwargs={'slug': self.slug, })

    # def save(self, *args, **kwargs):
    #     try:
    #         new_image = compress(self.banner)
    #         # new_image = newPath(imgPath ,compressedImg)
    #         self.banner = new_image
    #     except ValueError:
    #         pass
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.blockName