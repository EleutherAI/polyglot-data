import py_vncorenlp
import sys, getopt

vncorenlp_path = './vncorenlp'

py_vncorenlp.download_model(save_dir=vncorenlp_path)
model = py_vncorenlp.VnCoreNLP(save_dir=vncorenlp_path)



def main():
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('word_tokenize_corpus.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('word_tokenize_corpus.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        model.annotate_file(input_file = input_file, output_file = output_file)

if __name__=="__main__":
    main()
