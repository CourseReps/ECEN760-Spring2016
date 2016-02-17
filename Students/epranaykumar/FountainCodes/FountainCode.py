__author__ = 'pranaykumar eedara'

import numpy as np
import FC_Decoder
import FC_Encoder
import matplotlib.pyplot as plt

import timeit


# Required parameters
total_src_packets = 1000 # K
err_bound= 0.05  # delta 0.05
c= 0.1

#Maximum number of encoded packets to generate
N= total_src_packets *2

# create  k number of  source bits (i.e., 1000)
src_values=np.random.random_integers(0,1, total_src_packets)
print "------Source Packets--------"
print src_values

# Function of Average number of recovered packets with length
mean_recovrd_pkts_with_len = np.zeros(N+1)
freq_total_nodes_utilised = np.zeros(N+1)
trials=100
time_old = timeit.default_timer()

for i in range(trials):

    print "\n------------Trial "+str(i)+' -------------'

    #### Encoding
    print "\n-------During Encoding ------"
    encoder = FC_Encoder.Encoder(src_values,err_bound, c)
    encoded_Graph, encoded_values = encoder.Encode(N) # N: maximum number of encoded packets to generate

    #print "\nEncoded graph \n",encoded_Graph.edges()
    #print "\nEncoded values \n",encoded_values


    ### Decoding
    print "\n-------During Decoding ------"
    decoder = FC_Decoder.Decoder(encoded_Graph,encoded_values)
    decoded_src_values, recovrd_pkts_with_len , total_encoded_nodes_utilised = decoder.Decode(N)

    #print "\nDecoded values \n",decoded_src_values
    print "\nNumber of Errors in decoded packets "
    print np.sum(abs(decoded_src_values-src_values))

    mean_recovrd_pkts_with_len += np.array(recovrd_pkts_with_len)
    freq_total_nodes_utilised[total_encoded_nodes_utilised] += 1;



mean_recovrd_pkts_with_len = mean_recovrd_pkts_with_len/trials
index =range(N+1)

print(timeit.default_timer()-time_old)

#plot recovrd_pkts_with_len
fig = plt.figure(1)
ax = plt.subplot(111)
rects1 = ax.bar(index, mean_recovrd_pkts_with_len, width=1, color='r')
ax.set_ylabel('Recovered Packets')
ax.set_title('K='+str(total_src_packets)+' Trials='+str(trials)+ ' 0.05,0.1')
ax.set_xlabel('Utilised encoded packets')

fig2 = plt.figure(2)
ax2 = plt.subplot(111)
rects2 = ax2.bar(index, freq_total_nodes_utilised, width=1, color='r')
ax2.set_ylabel('freq_total_nodes_utilised')
ax2.set_title('K='+str(total_src_packets)+' Trials='+str(trials)+ ' 0.05,0.1')
ax2.set_xlabel('Utilised encoded packets')
plt.show()
