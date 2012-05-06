CC     := gcc
CXX    := g++
LD     := g++
AR     := ar rc
RANLIB := ranlib

CXXFLAGS  := -Wall -O3
LDFLAGS   := -Wall -O3
LIBS      :=

OUTPUT += p3

all: $(OUTPUT)

SRCS += p3.cpp

OBJS += $(addsuffix .o,$(basename $(SRCS)))

$(OUTPUT): $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS) 

$(OUTPUTLIB): $(OBJS)
	      $(AR) $@ $(OBJS)
	      $(RANLIB) $@

clean:
	rm $(OBJS) $(OUTPUT) *~ -rf

