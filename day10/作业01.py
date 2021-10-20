pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
linuxs={'wupeiqi','oldboy','gangdan'}
print(pythons & linuxs)
print(pythons.intersection(linuxs))
print(pythons | linuxs)
print(pythons.union(linuxs))
print(pythons - linuxs)
print(pythons.difference(linuxs))
print(pythons.symmetric_difference(linuxs))
print(pythons ^ linuxs)