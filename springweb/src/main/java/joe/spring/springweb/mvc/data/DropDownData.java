package joe.spring.springweb.mvc.data;

public class DropDownData {

	protected Long id;
	protected String idStr;
	protected String name;
	public DropDownData() {
		super();
		// TODO Auto-generated constructor stub
	}
	public DropDownData(Long id, String idStr, String name) {
		super();
		this.id = id;
		this.idStr = idStr;
		this.name = name;
	}
	public DropDownData(Long id, String name) {
		super();
		this.id = id;
		this.name = name;
	}
	public DropDownData(String idStr, String name) {
		super();
		this.idStr = idStr;
		this.name = name;
	}
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getIdStr() {
		return idStr;
	}
	public void setIdStr(String idStr) {
		this.idStr = idStr;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((id == null) ? 0 : id.hashCode());
		result = prime * result + ((idStr == null) ? 0 : idStr.hashCode());
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		DropDownData other = (DropDownData) obj;
		if (id == null) {
			if (other.id != null)
				return false;
		} else if (!id.equals(other.id))
			return false;
		if (idStr == null) {
			if (other.idStr != null)
				return false;
		} else if (!idStr.equals(other.idStr))
			return false;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		return true;
	}
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("DropDownData [id=");
		builder.append(id);
		builder.append(", idStr=");
		builder.append(idStr);
		builder.append(", name=");
		builder.append(name);
		builder.append("]");
		return builder.toString();
	}
	
}
