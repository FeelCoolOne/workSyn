# encoding=utf-8
import matplotlib.pyplot as plt
import matplotlib
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


def analysis_data(data):
    matplotlib.rc('xtick', labelsize=16)
    # dataframe = data.fillna('null')
    dataframe = data
    for index in dataframe.columns:
        plt.figure(index)
        plt.title('{0}统计分布'.format(index))
        plt.xlabel(index, fontsize=16)
        plt.ylabel('num')
        c = dataframe[index].value_counts(dropna=True)
        c.sort_values(ascending=False)[:50].plot('bar')
        try:
            dataframe[index].fillna('null', inplace=True)
            print '{0}":"{1}'.format(index, float(dataframe[index].value_counts(dropna=False)['null']) / dataframe[index].size)
        except:
            print index, 'no nan'
    plt.show()


def main():
    import cPickle as pickle
    data = {}
    with open('../data/id.dat', 'rb') as f:
        data = pickle.load(f)
    if len(data) == 0:
        print 'data source error'
        exit()


if __name__ == '__main__':
    main()
'''
    import cPickle as pickle
    from get_id_model import Video
    data = {}
    with open('../data/id.dat', 'rb') as f:
        data = pickle.load(f)
    if len(data) == 0:
        print 'data source error'
        exit()
    handler = Video()
    dataframe = data['tv']
    analysis_data(dataframe)
'''
