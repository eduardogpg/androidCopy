require 'fileutils'

class Copiar
	def initialize()
	end
	def copiar()
		desde = ARGV[0]
		hasta = ARGV[1]
		puts desde
		puts hasta

		FileUtils.cp_r(Dir[desde+"/*"],hasta)
	end
	
end

objeto = Copiar.new()
objeto.copiar