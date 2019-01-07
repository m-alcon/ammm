import matplotlib.pyplot as plt

def save_plot(data,name):
    color = ['b','g','r','c','m','y']
    marker = ['o','o','o','^','^','s']
    markersize = 13
    fig, ax = plt.subplots()
    ax.plot(data['Greedy'][0],data['Greedy'][1],marker=marker[0], markerfacecolor=color[0], markeredgecolor=color[0], markersize=markersize, label='Greedy', linestyle='None')
    ax.plot(data['Greedy LS FI'][0],data['Greedy LS FI'][1],marker=marker[1], markerfacecolor=color[1], markeredgecolor=color[1], markersize=markersize, label='Greedy LS FI', linestyle='None')
    ax.plot(data['Greedy LS BI'][0],data['Greedy LS BI'][1],marker=marker[2], markerfacecolor=color[2], markeredgecolor=color[2], markersize=markersize, label='Greedy LS BI', linestyle='None')
    ax.plot(data['GRASP LS FI'][0],data['GRASP LS FI'][1],marker=marker[3], markerfacecolor=color[3], markeredgecolor=color[3], markersize=markersize, label='GRASP LS FI', linestyle='None')
    ax.plot(data['GRASP LS BI'][0],data['GRASP LS BI'][1],marker=marker[4], markerfacecolor=color[4], markeredgecolor=color[4], markersize=markersize, label='GRASP LS BI', linestyle='None')
    ax.plot(data['CPLEX'][0],data['CPLEX'][1],marker=marker[5], markerfacecolor=color[5], markeredgecolor=color[5], markersize=markersize, label='CPLEX', linestyle='None')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('GAP (%)')
    ax.set_ylim(-2,30)
    ax.legend(loc='best', shadow=False, fontsize=11)
    plt.savefig('./img/%s.png'%name)

small = {}
small['Greedy'] = [0.0549,21.98]
small['Greedy LS FI'] = [0.4401,21.98]
small['Greedy LS BI'] = [0.4465,21.98]
small['GRASP LS FI'] = [41.394,20.47]
small['GRASP LS BI'] = [18.926,19.61]
small['CPLEX'] = [28.060,0]

medium = {}
medium['Greedy'] = [0.2635,26.58]
medium['Greedy LS FI'] = [1.2593,26.58]
medium['Greedy LS BI'] = [1.2288,26.58]
medium['GRASP LS FI'] = [6.918,25.17]
medium['GRASP LS BI'] = [234.59,25.44]
medium['CPLEX'] = [461.27,0]

big = {}
big['Greedy'] = [0.6846,14.51]
big['Greedy LS FI'] = [3.3543,14.51]
big['Greedy LS BI'] = [3.5170,14.51]
big['GRASP LS FI'] = [40.161,13.80]
big['GRASP LS BI'] = [160.78,14.31]
big['CPLEX'] = [1572.8,0]

huge = {}
huge['Greedy'] = [1.8729,23.14]
huge['Greedy LS FI'] = [8.3487,23.14]
huge['Greedy LS BI'] = [8.3637,23.14]
huge['GRASP LS FI'] = [8.2651,23.12]
huge['GRASP LS BI'] = [8.2874,23.19]
huge['CPLEX'] = [2925.2,0]

giant = {}
giant['Greedy'] = [3.1425,17.22]
giant['Greedy LS FI'] = [16.723,17.22]
giant['Greedy LS BI'] = [16.748,17.22]
giant['GRASP LS FI'] = []
giant['GRASP LS BI'] = [326.20,16.70]
giant['CPLEX'] = [4133.0,0]

if __name__ == '__main__':
    save_plot(small,'small')
    save_plot(medium,'medium')
    save_plot(big,'big')
    save_plot(huge,'huge')
    # save_plot(giant,'giant')