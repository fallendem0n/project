import app
import localeInfo
app.ServerName = None

SERVER_NAME = "Oden2"


SRV1 = {
	"name":"Siverp2",
	"name1":"Siverp2-Test",
	"host":"78.135.90.109",
	"host1":"78.135.90.109",
	"auth1":11010,
	"ch1":12100,
	"ch2":12200,
	"ch3":12300,
	"ch4":12400,
}

STATE_NONE = "..."

STATE_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

we1 = {
	1:{"key":11,"name":"Kanal 1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"Kanal 2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"Kanal 3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":14,"name":"Kanal 4","ip":SRV1["host"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
}

we2 = {
	1:{"key":11,"name":"Kanal 1","ip":SRV1["host1"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"Kanal 2","ip":SRV1["host1"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"Kanal 3","ip":SRV1["host1"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":14,"name":"Kanal 4","ip":SRV1["host1"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : SRV1["name"],
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
		2 : { "ip":SRV1["host1"], "port":SRV1["auth1"], },
	}
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : we1, },
		2 : { "name" :SRV1["name1"], "channel" : we2, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
	20 : { "ip" : SRV1["host1"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
}

TESTADDR = { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }
TESTADDR = { "ip" : SRV1["host1"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }

#DONE


