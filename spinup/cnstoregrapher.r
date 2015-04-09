options(echo=TRUE) # if you want see commands in output file
args <- commandArgs(trailingOnly = TRUE)
print(args)
# trailingOnly=TRUE means that only your arguments are returned, check:
# print(commandsArgs(trailingOnly=FALSE))


filename <- args[1]
pdffile <- args[2]
rm(args)

pdf(file=pdffile)


# Some computations:
growthDaily = read.table(filename, header=T)
plot(growthDaily$soiln)
plot(growthDaily$soilc)
dev.off()
