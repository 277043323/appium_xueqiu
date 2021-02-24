import yaml

t = open("test.yaml")
m = yaml.safe_load(t)
print(m)