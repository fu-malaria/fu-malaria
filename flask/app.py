import os
from os import listdir
from os.path import isfile, join
from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
from werkzeug.utils import secure_filename
import detector

UPLOAD_FOLDER = 'static/uploads/'
PROCESS_FOLDER = 'static/processed/'

GALLERY_RAW_FOLDER = 'static/gallery/'
GALLERY_PROC_FOLDER = 'static/gallery/'

THICK_GALLERY = 'imgThickBlood'
THIN_GALLERY = 'imgThinBlood'

STATS_EXTENSION = '.stats'

ALLOWED_EXTENSIONS = set(['jpg','jpeg','png','gif','bmp', 'tif','webp'])
process_cmd = 'python detect/basic_detector.py '


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESS_FOLDER'] = PROCESS_FOLDER
app.config['GALLERY_RAW_FOLDER'] = GALLERY_RAW_FOLDER
app.config['GALLERY_PROC_FOLDER'] = GALLERY_PROC_FOLDER
app.config['THICK_GALLERY'] = THICK_GALLERY
app.config['THIN_GALLERY'] = THIN_GALLERY
app.config['STATS_EXTENSION'] = STATS_EXTENSION
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'my secret malaria key'
tolerance = 50

# Index page handler
@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      # check if the post request has the file part
      if 'file' not in request.files:
         flash('No file part')
         return redirect(request.url)
      file = request.files['file']
      # if user does not select file, browser also
      # submit a empty part without filename
      if file.filename == '':
         flash('No selected file')
         return redirect(request.url)
      else : #file and allowed_file(file.filename)
         filename = secure_filename(file.filename)
         inpath = app.config['UPLOAD_FOLDER']
         outpath = app.config['PROCESS_FOLDER']
         infile = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         outfile = os.path.join(app.config['PROCESS_FOLDER'], filename)
         file.save(infile)
         process_file(infile, outfile, str(tolerance))
         return redirect(url_for('view_processed', inpath=inpath, outpath=outpath, filename=filename))
   else:
      # Show thin sample gallery for user to view as an example
      gallery_path = app.config['GALLERY_PROC_FOLDER'] + app.config['THIN_GALLERY'] + 'Input/'
      files = get_files(gallery_path)
      return render_template('index.html', gallery_files=files, upload_path=gallery_path)


# Show processed file (redirect from index page file upload form)
@app.route('/view_processed/<filename>')
def view_processed(filename):
   inpath = app.config['UPLOAD_FOLDER']
   outpath = app.config['PROCESS_FOLDER']
   red, malaria = get_stats(outpath, filename)
   return render_template('process.html', input_file=inpath, output_file=outpath, filename=filename, red=red, malaria=malaria)


# Show processed file (redirect from index page gallery)
@app.route('/mini_gallery/<filename>')
def mini_gallery(filename):
   inpath = app.config['GALLERY_RAW_FOLDER'] + app.config['THIN_GALLERY'] + 'Input/'
   outpath = app.config['GALLERY_PROC_FOLDER'] + app.config['THIN_GALLERY'] + 'Output/'
   red, malaria = get_stats(outpath, filename)
   return render_template('process.html', input_file=inpath, output_file=outpath, filename=filename, red=red, malaria=malaria)

# Gallery handler
@app.route('/gallery', methods=['GET','POST'])
def gallery():
   if request.method == 'POST':
      threshold = request.form.get('thresholdRadio')
      gallery = request.form.get('galleryRadio')

      if int(threshold) < 0 or int(threshold) > 100:
         return render_template('gallery.html')

      if not 'thin' in gallery and not 'thick' in gallery:
         return render_template('gallery.html')

      if 'thin' in gallery:
         inpath = app.config['GALLERY_RAW_FOLDER'] + app.config['THIN_GALLERY'] + 'Input/'
         outpath = app.config['GALLERY_PROC_FOLDER'] + app.config['THIN_GALLERY'] + 'Output/'
      else:
         inpath = app.config['GALLERY_RAW_FOLDER'] + app.config['THICK_GALLERY'] + 'Input/'
         outpath = app.config['GALLERY_PROC_FOLDER'] + app.config['THICK_GALLERY'] + 'Output/'

      files = get_files(inpath)
      
      for f in files:
         process_file(inpath+'/'+f, outpath+'/'+f, str(threshold))

      return render_template('gallery.html', gallery_list=files, gallery_inpath=inpath, gallery_outpath=outpath)

   else: 
      inpath = app.config['GALLERY_RAW_FOLDER'] + app.config['THIN_GALLERY'] + 'Input/'
      outpath = app.config['GALLERY_PROC_FOLDER'] + app.config['THIN_GALLERY'] + 'Output/'
      files = get_files(inpath)
      return render_template('gallery.html', gallery_list=files, gallery_inpath=inpath, gallery_outpath=outpath)


# Gets list of image files excluding .stats files
def get_files(gallery_path):
   files = [f for f in listdir(gallery_path) if isfile(join(gallery_path, f))]
   files = [f for f in files if allowed_file(f)]
   return files


# Do malaria detection image processing
def process_file(inpath, outpath, threshold):   
   detector.process(inpath, outpath, str(threshold))


# Simple validation of files allowed for upload based on file extension
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

# Get stats about processed image from file
# Saving stats to file as database not really necessary, and avoiding re-processing to get stats
def get_stats(outpath, filename):
   statsfile = outpath+'/'+filename+app.config['STATS_EXTENSION']
   red = 0
   malaria = 0
   with open(statsfile, mode='r') as f:
      red = f.readline()
      malaria = f.readline()
   return red, malaria


if __name__ == '__main__':
   app.run(debug=True)
